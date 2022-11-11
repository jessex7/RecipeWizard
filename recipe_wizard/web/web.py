from datetime import datetime, timezone
from flask import Blueprint, current_app, request, redirect, url_for, render_template, abort
from sqlalchemy.sql.expression import select, delete
from recipe_wizard.database import db
from recipe_wizard.models import Recipe
from recipe_wizard.schema import RecipeSchema

bp = Blueprint("web_api_bp", __name__)
front_version = current_app.config.get("FRONT_VERSION")


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
    session = db.session
    try:
        new_recipe = Recipe()
        new_recipe.name = request.form["name"]
        new_recipe.ingredients = request.form["ingredients"]
        new_recipe.instructions = request.form["instructions"]
        if request.form["author"] is not None:
            new_recipe.author = request.form["author"]
        if request.form["rating"] is not None:
            new_recipe.rating = request.form["rating"]
        if "prep_time" in request.form:
            new_recipe.prep_time = request.form["prep_time"]
        if "cook_time" in request.form:
            new_recipe.cook_time = request.form["cook_time"]
        new_recipe.created_at = datetime.now(timezone.utc)
        new_recipe.modified_at = new_recipe.created_at
        session.add(new_recipe)
        session.commit()
        return redirect(url_for("web_api_bp.get_recipes_page"))
    except Exception as error:
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
    try:
        stmt = (
            select(Recipe)
            .where(Recipe.recipe_id == recipe_id)
        )
        recipe = session.execute(stmt).scalar()
        
        recipe.name = request.form["name"]
        recipe.ingredients = request.form["ingredients"]
        recipe.instructions = request.form["instructions"]
        if "author" in request.form:
            recipe.author = request.form["author"]
        if "rating" in request.form:
            recipe.rating = request.form["rating"]
        if "prep_time" in request.form:
            recipe.prep_time = float(request.form["prep_time"])
        if "cook_time" in request.form:
            recipe.cook_time = request.form["cook_time"]
        recipe.modified_at = datetime.now(timezone.utc)
        session.commit()
        return redirect(url_for("web_api_bp.get_recipes_page"))
    except Exception as error:
        print(error)
        abort(404)

@bp.post(f"/front/{front_version}/recipes/<int:recipe_id>/delete")
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
