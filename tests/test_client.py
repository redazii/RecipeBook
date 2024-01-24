import pytest
from fastapi.testclient import TestClient
from recipes.schema_dto import Recipe
from main import app  


client = TestClient(app)

# Définir des données de test
user_data = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjViNjAyZTBjYTFmNDdhOGViZmQxMTYwNGQ5Y2JmMDZmNGQ0NWY4MmIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbXlhcGktOGEzNDAiLCJhdWQiOiJteWFwaS04YTM0MCIsImF1dGhfdGltZSI6MTcwNjEwMDc2OCwidXNlcl9pZCI6Inl0bEtvbXdVWXJaU1h5SXVPRGZ2cGw3NHFyMTIiLCJzdWIiOiJ5dGxLb213VVlyWlNYeUl1T0RmdnBsNzRxcjEyIiwiaWF0IjoxNzA2MTAwNzY4LCJleHAiOjE3MDYxMDQzNjgsImVtYWlsIjoic3RyaW5nQGxpdmUuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbInN0cmluZ0BsaXZlLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.h_L8O8lr8x4J-ZvtrHlrjugulZ_ynjARqWxxeLis7f8z8P-EfX27L9z-xCDp6k4NDXWUsN-OUtFlC5j1NkfDDdYcs0aiZmgOuAmmGSNqCk9Rx_CYweXL9meevDLOO_ZHLwox6SuGDv9mUFsZa_KdlD3GRaXVoSqFMwohjVIH0dY-l1w1uv-oRxlDHNPvRQz31vRwgEYWw8CJR7ckXnuji-8_N8vbGZlt16VmAT-slC5vDxTQ-30Mxa4l43MHrPABcXFXCGvmSOxvAVflhiOnnSgIo2V7cSJ9pBrJsCGQUBzBNBgIp084pkZs1UedBWmCTcylWdfB755Ti3ycO3ZNCw"}  

# Tester l'endpoint d'affichage des recettes
def test_display_recipes():
    response = client.get("/recipes/", headers=user_data)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Tester l'endpoint d'ajout de recette
def test_add_recipe():
    new_recipe = Recipe(name= "Test Recipe", ingredients=["Ingredient 1", "Ingredient 2"], instructions="Mis and Cook", category= "Test Category", id="")
    response = client.post("/recipes/add-recipe/", json=new_recipe.model_dump(), headers=user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Recipe added successfully"}

# Tester l'endpoint de recherche par nom
def test_get_recipe_by_name():
    response = client.get("/recipes/name/Salade César", headers=user_data)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Tester l'endpoint de recherche par catégorie
def test_get_recipe_by_category():
    response = client.get("/recipes/category/Salade", headers=user_data)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Tester l'endpoint de récupération par ID
def test_get_recipe_by_id():
    response = client.get("/recipes/c58bb370-1054-4ee0-aa1f-b57d2ec39dae", headers=user_data) 
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Tester l'endpoint de suppression par ID
def test_delete_recipe():
    response = client.delete("/recipes/d95f3750-45c6-4ad3-844e-dc00a79b2ca0", headers=user_data)  
    assert response.status_code == 200
    assert response.json() == {"message": "recipe deleted"}

# Tester l'endpoint de mise à jour par ID
def test_update_recipe():
    updated_data = {"category": "Updated Category"}
    response = client.patch("/recipes/c58bb370-1054-4ee0-aa1f-b57d2ec39dae", json=updated_data, headers=user_data)  # Remplacez par un vrai ID de recette
    assert response.status_code == 200
    assert response.json() == {"message": "Recipe updated successfully"}
