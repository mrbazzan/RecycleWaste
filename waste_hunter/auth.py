
from flask import Blueprint, render_template, request, flash, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from waste_hunter.db import User, db

bp = Blueprint('auth', __name__, url_prefix='')


@bp.route("/signup", methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        error = None
        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        elif not email:
            error = 'Email is required'
        elif User.query.filter_by(email=email).first():
            error = 'Email {} is already registered'.format(email)
        elif User.query.filter_by(username=username).first():
            error = "User {} is already registered".format(username)
        elif password != confirm_password:
            error = 'Incorrect password'

        if error is None:
            user = User(username=username, password=generate_password_hash(password), email=email)
            db.session.add(user)
            db.session.commit()
            return redirect('index')

        flash(error)

    return render_template("waste_hunter/WasteHunterSignUp.html")


@bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    return render_template("waste_hunter/WasteHunterLogin.html")
