
import click

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask.cli import with_appcontext


db = SQLAlchemy()


@click.command('init-db')
@with_appcontext
def init_db_command():
    db.create_all()
    click.echo('Initialized the database')


def initialize_app(app):
    app.cli.add_command(init_db_command)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __str__(self):
        return self.username
