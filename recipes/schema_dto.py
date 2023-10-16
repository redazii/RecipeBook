import datetime
from pydantic import BaseModel

# Modèle Pydantic pour une recette
class Recipe(BaseModel):
    id: str
    name: str
    ingredients: list  # Liste d'ingrédients
    instructions: str  # Instructions de préparation
    cooking_time: int  # Temps de cuisson en minutes
    created_at: datetime.datetime

# Modèle Pydantic pour POST (ajouter une recette)
class RecipeCreate(BaseModel):
    name: str
    ingredients: list
    instructions: str
    cooking_time: int

# Modèle Pydantic pour la mise à jour d'une recette
class RecipeUpdate(BaseModel):
    name: str
    ingredients: list
    instructions: str
    cooking_time: int

# Modèle Pydantic pour une liste de recettes
class RecipeList(BaseModel):
    recipes: List[Recipe]
