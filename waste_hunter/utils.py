
import functools
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
