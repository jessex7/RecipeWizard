"""Declares models using sqlalchemy object relational paradigm

Good reference material: https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html
"""

from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime, String, Float, Integer
from sqlalchemy.sql.schema import Column, ForeignKey
from recipe_wizard.database import Base


class Recipe(Base):
    __tablename__ = "recipe"
    recipe_id = Column(Integer, primary_key=True) 
    name = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    rating = Column(Integer)
    image_location = Column(String)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    author = Column(String)
    prep_time = Column(Float)
    cook_time = Column(Float)
    ingredients = relationship(
        "Ingredient", cascade="all, delete-orphan"
    )

class Ingredient(Base):
    __tablename__ = "ingredient"
    ingredient_id = Column(Integer, primary_key=True)
    recipe_id = Column(
        Integer, ForeignKey("recipe.recipe_id", ondelete="CASCADE", onupdate="CASCADE")
    )
    name = Column(String, nullable=False)
    serving_unit = Column(String)
    serving_size = Column(String)



