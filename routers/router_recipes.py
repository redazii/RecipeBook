from fastapi import APIRouter, HTTPException
from recipes.schema_dto import Recipe
from database.firebase import db
from typing import List


router = APIRouter(
    prefix='/recipes',
    tags=["Recipes"]
)

recipes = []
   


# Endpoint to display all recipes (GET)
@router.get("/")
def display_recipes():
    recipes_data = db.child("recipes").get().val()
    if recipes_data is not None:
     return recipes_data


# Endpoint to delete a recipe by name (DELETE)
@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: str):
    recipes_data = db.child("recipes").child(recipe_id).get()
    if recipes_data is not None :
     db.child("recipes").child(recipe_id).remove()
     return {"message":"recipe deleted"}
    else:
      raise HTTPException(status_code=404,detail="recipe not found")
    


# Endpoint to add a recipe (POST) 
@router.post("/add-recipe/")
def add_recipe(recipe: Recipe):
    recipe_id = recipe.id
    name = recipe.name
    recipe_data = recipe.dict()
    recipes.append(recipe)
    db.child("recipes").child(recipe_id).set(recipe_data)
    db.child("recipes").child(name).set(recipe_data)
    return {"message": "Recipe added successfully"}

# Endpoint pour récupérer une recette par son ID (GET)
@router.get("/{recipe_id}")
def get_recipe_by_id(recipe_id: int):
    recipes_data = db.child("recipes").child(recipe_id).get()
    if recipes_data is not None :
     return recipes_data.val()
    else:
      raise HTTPException(status_code=404,detail="recipe not found")
      
# Endpoint pour récupérer une recette par son nom (GET)
@router.get("/name")
def get_recipe_by_name(name: str):
  search_result = []
  recipes =  db.child("recipes").get()
  for recipe in recipes:
   if name in recipe['name'].lower():
    search_result.append(recipe)
    continue
   return search_result

@router.patch("/{recipe_id}")
def update_recipe(recipe_id: str, updated_recipe_data: dict):
    # Récupérer les données de la recette spécifique
    recipe_data = db.child("recipes").child(recipe_id).get()

    # Vérifier si la recette existe
    if recipe_data.val():
        # Mettre à jour les champs spécifiés dans updated_recipe_data
        db.child("recipes").child(recipe_id).update(updated_recipe_data)
        return {"message": "Recipe updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Recipe not found")
