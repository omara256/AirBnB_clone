#!/usr/bin/python3
"""
 class Review which inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ define a User class """
    place_id = ""
    user_id = ""
    text = ""
