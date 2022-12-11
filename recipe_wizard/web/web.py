from datetime import datetime, timezone
from flask import Blueprint, current_app, request, redirect, url_for, render_template, abort
from sqlalchemy.sql.expression import select, delete, update
from recipe_wizard.database import db
from recipe_wizard.models import Recipe, Ingredient
from recipe_wizard.schema import RecipeSchema
from recipe_wizard.rest import rest_api

bp = Blueprint("web_api_bp", __name__)
front_version = current_app.config.get("FRONT_VERSION")


@bp.get(f"/front/{front_version}/recipes/<int:recipe_id>")
def get_recipe_page(recipe_id):
    session = db.session
    stmt = (
        select(Recipe)
        .where(Recipe.recipe_id==recipe_id)
    )
    result = session.execute(stmt)
    recipe = result.scalar() 
    formatted_recipe = RecipeSchema().dump(recipe)
    return render_template("recipes/index.html", recipes=formatted_recipe)

@bp.get(f"/front/{front_version}/recipes")
def get_recipes_page():
    session = db.session
    stmt = (
        select(Recipe)
    )
    result = session.execute(stmt)
    recipes = result.scalars()

    formatted_recipes = RecipeSchema().dump(recipes, many=True)
    return render_template("recipes/index.html", recipes=formatted_recipes)

@bp.get(f"/front/{front_version}/recipes/create")
def get_create_recipe_page():
    return render_template("recipes/create.html")

@bp.post(f"/front/{front_version}/recipes/create")
def create_recipe():
    try:
        incoming_data = request.get_json()
        schema = RecipeSchema()
        new_recipe = schema.load(incoming_data, session=db.session)
        db.session.add(new_recipe)
        db.session.commit()
        redirect(url_for(get_recipes_page()))
    except Exception as error:
        print(error.args)
        print(error)
        abort(404)

@bp.get(f"/front/{front_version}/recipes/<int:recipe_id>/edit")
def get_edit_recipe_page(recipe_id):
    session = db.session
    try:
        stmt = (
            select(Recipe)
            .where(Recipe.recipe_id == recipe_id)
        )
        recipe = session.execute(stmt).scalar()
        fmt_recipe = RecipeSchema().dump(recipe)
        return render_template("recipes/edit.html", recipe=fmt_recipe)
    except Exception as error:
        print(error)
        abort(404)

@bp.post(f"/front/{front_version}/recipes/<int:recipe_id>/edit")
def edit_recipe(recipe_id):
    session = db.session
    incoming_data = request.get_json()
    schema = RecipeSchema()
    new_recipe = schema.load(incoming_data, session=session)
    try:
        stmt = (
            select(Recipe)
            .where(Recipe.recipe_id == recipe_id)
        )
        recipe = session.execute(stmt).scalar()
        recipe.recipe_name = new_recipe.recipe_name
        recipe.prep_time = new_recipe.prep_time
        recipe.cook_time = new_recipe.cook_time
        recipe.image_location = new_recipe.image_location
        recipe.rating = new_recipe.rating
        recipe.instructions = new_recipe.instructions
        recipe.modified_at = datetime.now(timezone.utc)
        recipe.ingredients = new_recipe.ingredients 
        # NOTE - this is not "updating" each row in the ingredients table. it is
        # deleting existing rows and inserting new ones. Not sure if that is a problem
        # at this point or not

        session.commit()
        return redirect(url_for("web_api_bp.get_recipes_page"))
    except Exception as error:
        print(error)
        abort(404)

@bp.delete(f"/front/{front_version}/recipes/<int:recipe_id>")
def delete_recipe(recipe_id):
    session = db.session
    try:
        stmt = (
            delete(Recipe)
            .where(Recipe.recipe_id == recipe_id)
        )
        session.execute(stmt)
        session.commit()
        return redirect(url_for("web_api_bp.get_recipes_page"))
    except Exception as error:
        print(error)
        abort(404)
