from pydantic import BaseModel
from typing import List


class Recipe(BaseModel):
  id : int
  name: str
  ingredients: List[str]
  instructions: str
  