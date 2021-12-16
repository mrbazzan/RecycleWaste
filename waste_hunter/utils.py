
import functools
import smtplib
import os

from flask import g, redirect, url_for
from email_validator import validate_email, EmailNotValidError


def dont_allow_access_to_login_and_signup(view):
    @functools.wraps(view)  # What is happening here?
    def wrapped(**kwargs):
        if g.user is not None:
            return redirect(url_for('index'))
        return view(**kwargs)

    return wrapped


def email_validator(email):
    error = None
    try:
        validate_email(email)
    except EmailNotValidError as e:
        error = e

    return error


def authenticated_access(view):
    @functools.wraps(view)
    def wrapped(**kwargs):
        if g.user:
            return view(**kwargs)
        return redirect(url_for('index'))

    return wrapped


# TODO: each users should receive a * on every request pick-up.

def send_email(email, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('bazzanapalowo@gmail.com', os.environ.get('password'))

        server.sendmail('bazzanapalowo@gmail.com', email, message)
    except smtplib.SMTPAuthenticationError:
        return 0
    return 1
