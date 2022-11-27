from datetime import datetime
from marshmallow import ValidationError, fields, validates
from marshmallow.fields import DateTime
from marshmallow.decorators import post_load
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, load_instance_mixin

from recipe_wizard.models import (
    Recipe,
    Ingredient,
)


class IngredientSchema(SQLAlchemySchema):
    class Meta:
        model = Ingredient

    ingredient_id = auto_field()
    recipe_id = auto_field()
    name = auto_field()
    serving_unit = auto_field()
    servings = auto_field()

class RecipeSchema(SQLAlchemySchema):
    class Meta:
        model = Recipe

    recipe_id = auto_field()
    name = auto_field()
    prep_time = auto_field()
    cook_time = auto_field()
    rating = auto_field()
    image_location = auto_field()
    created_at = auto_field()
    modified_at = auto_field()
    author = auto_field()
    ingredients = fields.Nested(IngredientSchema(exclude=("recipe_id",)), many=True)
    instructions = auto_field()
