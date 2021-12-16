
import os
from flask import Flask, render_template, request, g


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'waste_hunter.sqlite')
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db, auth
    from .utils import authenticated_access, send_email

    db.db.init_app(app)
    db.migrate.init_app(app, db.db)
    app.register_blueprint(auth.bp)

    app.add_url_rule('/', endpoint='index')

    #TODO; Redo index page, send using email, deploy to heroku

    @app.route("/")
    def index():
        return render_template("user_profile/index.html")

    @app.route("/request", methods=('GET', 'POST'))
    @authenticated_access
    def hello():
        if request.method == 'POST':
            location = request.form['pickup_location']
            description = request.form['waste_description']

            if send_email('abdulwasiuapalowo@gmail.com', location + '\n' + description):
                return "Success"

        return render_template("waste_hunter/WasteHunterRequestPickUp.html")

    @app.route('/report', methods=('GET', 'POST'))
    @authenticated_access
    def report():
        if request.method == 'POST':
            location = request.form['dump_location']
            description = request.form['waste_description']

            if send_email('abdulwasiuapalowo@gmail.com', location + '\n' + description):
                return "Success"
        return render_template("waste_hunter/WasteHunterReport.html")

    return app
