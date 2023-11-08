from pydantic import BaseModel
from typing import List


class Recipe(BaseModel):
  id : str
  name: str
  ingredients: List[str]
  instructions: str
  category: str

  