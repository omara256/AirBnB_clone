#!usr/bin/python3

"""
  this is the first user creation
  
"""

from models.base_model import BaseModel

class user(modelbase):
  """ defining our user's parameters"""
  email = ""
  password = ""
  first_name = ""
  last_name = ""
