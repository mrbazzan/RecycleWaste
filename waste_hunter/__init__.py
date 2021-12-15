
import os
from flask import Flask, render_template


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

    db.db.init_app(app)
    db.initialize_app(app)
    app.register_blueprint(auth.bp)

    app.add_url_rule('/', endpoint='index')

    @app.route("/")
    def index():
        return render_template("user_profile/index.html")

    return app
