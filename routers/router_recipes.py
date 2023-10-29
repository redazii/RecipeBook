from fastapi import APIRouter
from recipes.schema_dto import Recipe

router = APIRouter(
    prefix='/recipes',
    tags=["Recipes"]
)

recipes = []
   


# Endpoint to display all recipes (GET)
@router.get("/recipes/")
def display_recipes():
    return recipes


# Endpoint to delete a recipe by name (DELETE)
@router.delete("/recipes/{name}")
def delete_recipe(name: str):
    global recipes
    recipes = [recipe for recipe in recipes if recipe.name != name]
    return {"message": f"Recipe with the name '{name}' deleted successfully"}


# Endpoint to add a recipe (POST)
@router.post("/add-recipe/")
def add_recipe(recipe: Recipe):
    recipes.append(recipe)
    return {"message": "Recipe added successfully"}