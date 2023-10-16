from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from recipes.schema_dto import Recipe, RecipeNoID

router = APIRouter(
    prefix='/recipes',
    tags=["Recipes"]
)

recipes = [
    Recipe(id="recipe1", name="Spaghetti Bolognese", ingredients=["spaghetti", "ground beef", "tomato sauce"]),
    Recipe(id="recipe2", name="Chicken Alfredo", ingredients=["chicken", "fettuccine pasta", "alfredo sauce"]),
    Recipe(id="recipe3", name="Vegetable Stir-Fry", ingredients=["mixed vegetables", "soy sauce", "rice"])
]

@router.get('/', response_model=List[Recipe])
async def get_recipes():
    """List all the recipes."""
    return recipes

@router.post('/', response_model=Recipe, status_code=201)
async def create_recipe(new_recipe: RecipeNoID):
    generated_id = uuid.uuid4()
    new_recipe = Recipe(id=str(generated_id), **new_recipe.dict())
    recipes.append(new_recipe)
    return new_recipe

@router.get('/{recipe_id}', response_model=Recipe)
async def get_recipe_by_id(recipe_id: str):
    for recipe in recipes:
        if recipe.id == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.patch('/{recipe_id}', status_code=204)
async def modify_recipe_name(recipe_id: str, modified_recipe: RecipeNoID):
    for recipe in recipes:
        if recipe.id == recipe_id:
            recipe.name = modified_recipe.name
            return
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.delete('/{recipe_id}', status_code=204)
async def delete_recipe(recipe_id: str):
    for recipe in recipes:
        if recipe.id == recipe_id:
            recipes.remove(recipe)
            return
    raise HTTPException(status_code=404, detail="Recipe not found")
