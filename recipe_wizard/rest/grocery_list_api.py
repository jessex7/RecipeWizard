from datetime import datetime, timezone
from flask import (
    Blueprint,
    current_app,
    request,
    jsonify,
    url_for,
)
from sqlalchemy.sql.expression import select, delete
from recipe_wizard.database import db
from recipe_wizard.models import Ingredient, GroceryList, GroceryItem
from recipe_wizard.schema import (
    GroceryListEndpointSchema,
    GroceryListSchema,
)

bp = Blueprint("grocery_list_api_bp", __name__)
api_version = current_app.config.get("API_VERSION")


@bp.get(f"/api/{api_version}/grocery")
def get_grocery_lists():
    session = db.session
    stmt = select(GroceryList)
    result = session.execute(stmt)
    grocery_lists = result.scalars()
    formatted_grocery_lists = GroceryListSchema().dump(grocery_lists, many=True)
    return {"data": formatted_grocery_lists}


@bp.get(f"/api/{api_version}/grocery/<int:grocery_list_id>")
def get_grocery_list(grocery_list_id, response_as_json=True):
    session = db.session
    stmt = select(GroceryList).where(GroceryList.grocery_list_id == grocery_list_id)
    result = session.execute(stmt)
    grocery_list = result.scalar()
    sorted_list = sorted(grocery_list.grocery_items, key=lambda i: (i.item))
    grocery_list.grocery_items = sorted_list

    if response_as_json:
        formatted_grocery_list = GroceryListSchema().dump(grocery_list, many=False)
        return {"data": formatted_grocery_list}
    else:
        return {"data": GroceryListSchema().dump(grocery_list, many=False)}


@bp.post(f"/api/{api_version}/grocery")
def post_recipes_for_grocery_list(request=None):
    json_data = request.get_json()
    session = db.session
    schema = GroceryListEndpointSchema()

    try:
        grocery_list_request = schema.load(json_data)

        grocery_list = GroceryList()
        grocery_list.created_at = datetime.now(timezone.utc)
        grocery_list.modified_at = grocery_list.created_at
        for id in grocery_list_request["recipe_ids"]:
            stmt = select(Ingredient).where(Ingredient.recipe_id == id)
            result = session.execute(stmt).scalars()
            for obj in result:
                grocery_item = GroceryItem()
                if obj.unit is not None and obj.unit != "" and obj.amount is not None:
                    grocery_item.item = (
                        f"{obj.ingredient_name} | {obj.amount} {obj.unit}"
                    )
                elif obj.unit is None and obj.amount is not None:
                    grocery_item.item = f"{obj.ingredient_name} | {obj.amount}"
                else:
                    grocery_item.item = f"{obj.ingredient_name}"
                grocery_list.grocery_items.append(grocery_item)
        session.add(grocery_list)
        session.commit()
        return {"data": grocery_list.grocery_list_id}

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


@bp.delete(f"/api/{api_version}/grocery/grocery-list/<int:grocery_list_id>")
def delete_grocery_list(grocery_list_id: int):
    session = db.session
    try:
        stmt = delete(GroceryList).where(GroceryList.grocery_list_id == grocery_list_id)
        result = session.execute(stmt)
    except Exception as err:
        print("error: %s" % err)
        return {"error": "INTERNAL_SERVER_ERROR"}, 500
