
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("user_profile/index.html")


@app.route("/login")
def login():
    return render_template("waste_hunter/WasteHunterLogin.html")


@app.route("/signup")
def signup():
    return render_template("waste_hunter/WasteHunterSignUp.html")
