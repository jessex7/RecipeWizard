from datetime import datetime
from marshmallow import ValidationError, fields, validates, Schema
from marshmallow.fields import DateTime
from marshmallow.decorators import post_load
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, load_instance_mixin
from marshmallow_sqlalchemy.fields import Nested



from recipe_wizard.models import (
    Recipe,
    Ingredient,
)


class IngredientSchema(SQLAlchemySchema):
    class Meta:
        model = Ingredient
        load_instance = True

    ingredient_id = auto_field()
    recipe_id = auto_field()
    ingredient_name = auto_field()
    unit = auto_field()
    amount = auto_field()

class RecipeSchema(SQLAlchemySchema):
    class Meta:
        model = Recipe
        load_instance = True
        include_relationships = True

    recipe_id = auto_field()
    recipe_name = auto_field()
    prep_time = auto_field()
    cook_time = auto_field()
    rating = auto_field()
    image_location = auto_field()
    created_at = auto_field()
    modified_at = auto_field()
    author = auto_field()
    # ingredients = fields.Nested(IngredientSchema(exclude=("recipe_id",)), many=True)
    ingredients = fields.List(Nested(IngredientSchema))
    instructions = auto_field()
