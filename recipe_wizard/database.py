from sqlalchemy.ext.declarative import declarative_base
import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()

def init_db():
    from recipe_wizard import models # why is this here?
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)

def register_database_commands(app):
    app.logger.info("registering database CLI commands to app")
    app.cli.add_command(init_db_command)

@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database")