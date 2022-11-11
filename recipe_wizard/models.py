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
    ingredients = Column(String, nullable=False)
    prep_time = Column(Float)
    cook_time = Column(Float)

