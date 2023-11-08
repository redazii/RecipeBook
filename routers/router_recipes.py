from fastapi import APIRouter, HTTPException , Depends
from recipes.schema_dto import Recipe
from routers.router_auth import get_current_user
from database.firebase import db
import uuid




router = APIRouter(
    prefix='/recipes',
    tags=["Recipes"]
)

recipes = []
   


# Endpoint to display all recipes (GET)
@router.get("/")
def display_recipes(user_data: int= Depends(get_current_user)): 
    recipes_data = db.child("recipes").get(user_data['idToken']).val()
    if recipes_data is not None:
     return [item for item in recipes_data.values()]
    


# Endpoint to add a recipe (POST) 
@router.post("/add-recipe/")
def add_recipe(recipe: Recipe,user_data: int= Depends(get_current_user)):
    uid = str(uuid.uuid4())
    recipe_id = uid
    name = recipe.name
    recipe_data = Recipe(id=uid, name=name, ingredients=recipe.ingredients,instructions=recipe.instructions,category=recipe.category)
    recipes.append(recipe)
    
    db.child("recipes").child(recipe_id).set(recipe_data.model_dump(), token=user_data['idToken'])
    return {"message": "Recipe added successfully"}

# Endpoint pour récupérer une recette par son nom (GET)
@router.get("/name/{name}")
def get_recipe_by_name(name: str ,user_data: int= Depends(get_current_user)):
  search_result = []
  recipes =  display_recipes(user_data=user_data)
  for recipe in recipes:
      if name in recipe['name'].lower():
       search_result.append(recipe)
  return search_result

# Endpoint pour récupérer une recette par son nom (GET)
@router.get("/category/{category}")
def get_recipe_by_category(category: str ,user_data: int= Depends(get_current_user)):
  search_result = []
  recipes =  display_recipes(user_data=user_data)
  for recipe in recipes:
      if category in recipe['category'].lower():
       search_result.append(recipe)
  return search_result

# Endpoint pour récupérer une recette par son ID (GET)
@router.get("/{recipe_id}")
def get_recipe_by_id(recipe_id: str, user_data: int= Depends(get_current_user)):
    recipes_data = db.child("recipes").child(recipe_id).get(user_data['idToken'])
    if recipes_data is not None :
     return recipes_data.val()
    else:
      raise HTTPException(status_code=404,detail="recipe not found")
    
# Endpoint to delete a recipe by name (DELETE)
@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: str, user_data: int= Depends(get_current_user)):
    recipes_data = db.child("recipes").child(recipe_id).get(user_data['idToken'])
    if recipes_data is not None :
     db.child("recipes").child(recipe_id).remove()
     return {"message":"recipe deleted"}
    else:
      raise HTTPException(status_code=404,detail="recipe not found")    
      

@router.patch("/{recipe_id}")
def update_recipe(recipe_id: str, updated_recipe_data: dict , user_data: int= Depends(get_current_user)):
    # Récupérer les données de la recette spécifique
    recipe_data = db.child("recipes").child(recipe_id).get(user_data['idToken'])

    # Vérifier si la recette existe
    if recipe_data.val():
        # Mettre à jour les champs spécifiés dans updated_recipe_data
        db.child("recipes").child(recipe_id).update(updated_recipe_data)
        return {"message": "Recipe updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Recipe not found")