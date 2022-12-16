"""Declares models using sqlalchemy object relational paradigm

Good reference material: https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html
"""

from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime, String, Float, Integer
from sqlalchemy.sql.schema import Column, ForeignKey
from recipe_wizard.database import Base


class Recipe(Base):
    __tablename__ = "recipe"
    recipe_id = Column(Integer, primary_key=True)
    recipe_name = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    rating = Column(Integer)
    image_location = Column(String)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    author = Column(String)
    prep_time = Column(String)
    cook_time = Column(String)
    ingredients = relationship("Ingredient", cascade="all, delete-orphan")


class Ingredient(Base):
    __tablename__ = "ingredient"
    ingredient_id = Column(Integer, primary_key=True)
    recipe_id = Column(
        Integer, ForeignKey("recipe.recipe_id", ondelete="CASCADE", onupdate="CASCADE")
    )
    ingredient_name = Column(String, nullable=False)
    unit = Column(String)
    amount = Column(Float)
