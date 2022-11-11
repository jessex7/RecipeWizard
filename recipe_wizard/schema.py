from datetime import datetime
from marshmallow import ValidationError, fields, validates
from marshmallow.fields import DateTime
from marshmallow.decorators import post_load
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, load_instance_mixin

from recipe_wizard.models import (
    Recipe,

)

class RecipeSchema(SQLAlchemySchema):
    class Meta:
        model = Recipe
        load_instance = True

    recipe_id = auto_field()
    name = auto_field()
    instructions = auto_field()
    ingredients = auto_field()
    prep_time = auto_field()
    cook_time = auto_field()
    rating = auto_field()
    image_location = auto_field()
    created_at = auto_field()
    modified_at = auto_field()
    author = auto_field()
