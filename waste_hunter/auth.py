
from flask import Blueprint, url_for, session, g, render_template, request, flash, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from waste_hunter.db import User, db

bp = Blueprint('auth', __name__, url_prefix='')


@bp.route("/signup", methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']
        password = request.form['password']

        error = None
        if not email:
            error = 'Email is required'
        elif not password:
            error = 'Password is required'
        elif User.query.filter_by(email=email).first():
            error = 'Email {} is already registered'.format(email)

        if error is None:
            user = User(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                address=address,
                password=generate_password_hash(password),
                email=email.strip()
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template("waste_hunter/WasteHunterSignUp.html")


@bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['password']
        error = None

        user = User.query.filter_by(email=email.strip()).first()

        if not email:
            error = "Email is required."
        elif not password:
            error = "Password is required"
        elif not confirm_password:
            error = "Confirm Password is required"

        if user is None:
            error = "Enter a valid user detail"
        elif not check_password_hash(user.password, password):
            error = "Incorrect password"

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))

        flash(error)

    return render_template("waste_hunter/WasteHunterLogin.html")
