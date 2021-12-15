
from flask import Blueprint, render_template, request
from waste_hunter.db import db

bp = Blueprint('auth', __name__, url_prefix='')


@bp.route("/signup", methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

    return render_template("waste_hunter/WasteHunterSignUp.html")


@bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    return render_template("waste_hunter/WasteHunterLogin.html")
