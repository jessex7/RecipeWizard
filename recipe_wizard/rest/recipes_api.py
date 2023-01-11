from datetime import datetime, timezone
from flask import (
    Blueprint,
    current_app,
    request,
)
from sqlalchemy.sql.expression import select, delete
from recipe_wizard.database import db
from recipe_wizard.models import Recipe, Ingredient
from recipe_wizard.schema import RecipeSchema

bp = Blueprint("recipes_api_bp", __name__)
api_version = current_app.config.get("API_VERSION")


@bp.get(f"/api/{api_version}/recipes")
def get_recipes():
    session = db.session
    stmt = select(Recipe)
    result = session.execute(stmt)
    recipes = result.scalars()
    formatted_recipes = RecipeSchema().dump(recipes, many=True)
    return {"data": formatted_recipes}


@bp.get(f"/api/{api_version}/recipes/<int:recipe_id>")
def get_recipes_by_id(recipe_id):
    session = db.session
    try:
        id = int(recipe_id)
        stmt = select(Recipe).where(Recipe.recipe_id == id)
        result = session.execute(stmt)
        scalar_recipes = result.scalars()
        formatted_recipe = RecipeSchema().dump(scalar_recipes, many=True)
        return {"data": formatted_recipe}
    except (TypeError, ValueError, KeyError) as error:
        print(error)
        return {"error": error}


@bp.post(f"/api/{api_version}/recipes")
def post_recipe():
    json_data = request.get_json()
    session = db.session
    try:
        new_recipe = Recipe()
        new_recipe.recipe_name = json_data["recipe_name"]
        for item in json_data["ingredients"]:
            ingredient = Ingredient()
            ingredient.ingredient_name = item["ingredient_name"]
            if "unit" in item:
                ingredient.unit = item["unit"]
            if "amount" in item:
                ingredient.amount = item["amount"]
            new_recipe.ingredients.append(ingredient)
        if "instructions" in json_data:
            new_recipe.instructions = json_data["instructions"]
        if "author" in json_data:
            new_recipe.author = json_data["author"]
        if "rating" in json_data:
            new_recipe.rating = json_data["rating"]
        if "prep_time" in json_data:
            new_recipe.prep_time = json_data["prep_time"]
        if "cook_time" in json_data:
            new_recipe.cook_time = json_data["cook_time"]
        new_recipe.created_at = datetime.now(timezone.utc)
        new_recipe.modified_at = new_recipe.created_at
        session.add(new_recipe)
        session.commit()
        formatted_recipe = RecipeSchema().dumps(new_recipe)
        return {"data": formatted_recipe}

    except KeyError as err:
        print("error: %s" % err)
        return {"error": "INVALID_REQUEST", "details": f"KeyError: {err.args[0]}"}, 400
    except ValueError as err:
        print("error: %s" % err)
        return {
            "error": "INVALID_REQUEST",
            "details": f"ValueError: {err.args[0]}",
        }, 400
    except Exception as err:
        print("error: %s" % err)
        return {"error": "INTERNAL_SERVER_ERROR"}, 500


@bp.put(f"/api/{api_version}/recipes/<int:recipe_id>")
def update_recipe(recipe_id):
    session = db.session
    json_data = request.get_json()
    try:
        id = int(recipe_id)
        stmt = select(Recipe).where(Recipe.recipe_id == id)
        result = session.execute(stmt)
        recipe = result.scalar()
        recipe.name = json_data["recipe_name"]
        for item in json_data["ingredients"]:
            ingredient = Ingredient()
            ingredient.ingredient_name = item["ingredient_name"]
            if "unit" in item:
                ingredient.unit = item["unit"]
            if "amount" in item:
                ingredient.amount = item["amount"]
            recipe.ingredients.append(ingredient)
        if "instructions" in json_data:
            recipe.instructions = json_data["instructions"]
        if "author" in json_data:
            recipe.author = json_data["author"]
        if "rating" in json_data:
            recipe.rating = json_data["rating"]
        if "prep_time" in json_data:
            recipe.prep_time = json_data["prep_time"]
        if "cook_time" in json_data:
            recipe.cook_time = json_data["cook_time"]
        recipe.modified_at = datetime.now(timezone.utc)
        session.commit()
        formatted_recipe = RecipeSchema().dumps(recipe)
        return {"data": formatted_recipe}

    except KeyError as err:
        print("error: %s" % err)
        return {"error": "INVALID_REQUEST", "details": f"KeyError: {err.args[0]}"}, 400
    except ValueError as err:
        print("error: %s" % err)
        return {
            "error": "INVALID_REQUEST",
            "details": f"ValueError: {err.args[0]}",
        }, 400
    except Exception as err:
        print("error: %s" % err)
        return {"error": "INTERNAL_SERVER_ERROR"}, 500


@bp.delete(f"/api/{api_version}/recipes/<int:recipe_id>")
def delete_recipe(recipe_id):
    session = db.session
    try:
        id = int(recipe_id)
        stmt = delete(Recipe).where(Recipe.recipe_id == id)
        session.execute(stmt)
        session.commit()
        return {}, 200
    except Exception as err:
        print("error: %s" % err)
        return {"error": "INTERNAL_SERVER_ERROR"}, 500
