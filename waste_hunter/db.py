
import click

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from flask.cli import with_appcontext


db = SQLAlchemy()
migrate = Migrate()


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
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    address = db.Column(db.String(200))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __str__(self):
        return self.last_name + ' ' + self.first_name
