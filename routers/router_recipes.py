import uuid
from fastapi import APIRouter, HTTPException
from recipes.schema_dto import Recipe, RecipeNoID

router = APIRouter(
    tags=["Recipes"]
)

# Liste de recettes fictives 
recipes = [
    Recipe(id="recipe1", name="Spaghetti Carbonara", ingredients=["pasta", "eggs", "cheese", "pancetta"]),
    Recipe(id="recipe2", name="Chicken Alfredo", ingredients=["chicken", "fettuccine", "cream", "Parmesan"]),
    Recipe(id="recipe3", name="Vegetable Stir-Fry", ingredients=["vegetables", "tofu", "soy sauce", "rice"]),
]

@router.get('/recipes')
async def get_recipes():
    return recipes

@router.post('/recipes')
async def create_recipe(recipe_data: RecipeNoID):
    new_recipe = Recipe(**recipe_data.dict(), id=str(uuid.uuid4()))
    recipes.append(new_recipe)
    return new_recipe

@router.get('/recipes/{recipe_id}')
async def get_recipe_by_id(recipe_id: str):
    for recipe in recipes:
        if recipe.id == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.patch('/recipes/{recipe_id}')
async def modify_recipe(recipe_id: str, modified_recipe_data: RecipeNoID):
    for recipe in recipes:
        if recipe.id == recipe_id:
            for key, value in modified_recipe_data.dict().items():
                setattr(recipe, key, value)
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.delete('/recipes/{recipe_id}', status_code=204)
async def delete_recipe(recipe_id: str):
    global recipes
    recipes = [recipe for recipe in recipes if recipe.id != recipe_id]
