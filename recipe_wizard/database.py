from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
import click
import json
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()


def init_db():
    from recipe_wizard import models  # why is this here?

    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)


def register_database_commands(app):
    app.logger.info("registering database CLI commands to app")
    app.cli.add_command(init_db_command)
    app.cli.add_command(insert_recipes_command)


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database")


@click.command("insert-dataset")
@click.argument("dataset")
@with_appcontext
def insert_recipes_command(dataset):
    insert_recipes(recipe_file=dataset)


# requires active app context
def insert_recipes(recipe_file):
    with open(recipe_file) as f:
        session = db.session
        data = json.load(f)
        for item in data:
            recipe = convert_recipe_dict_to_model(item)
            session.add(recipe)
        session.commit()


def convert_recipe_dict_to_model(input_dict):
    from recipe_wizard.models import Recipe, Ingredient

    timestamp = datetime.now(timezone.utc)
    recipe = Recipe()
    recipe.recipe_name = input_dict["recipe_name"]
    for item in input_dict["ingredients"]:
        ingredient = Ingredient()
        ingredient.ingredient_name = item["ingredient_name"]
        if "unit" in item:
            ingredient.unit = item["unit"]
        if "amount" in item:
            ingredient.amount = item["amount"]
        recipe.ingredients.append(ingredient)
    recipe.instructions = input_dict["instructions"]
    if "author" in input_dict:
        recipe.author = input_dict["author"]
    if "rating" in input_dict:
        recipe.rating = input_dict["rating"]
    if "cook_time" in input_dict:
        recipe.cook_time = input_dict["cook_time"]
    if "prep_time" in input_dict:
        recipe.prep_time = input_dict["prep_time"]
    recipe.created_at = timestamp
    recipe.modified_at = timestamp
    return recipe
