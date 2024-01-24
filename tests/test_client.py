import pytest
from fastapi.testclient import TestClient
from recipes.schema_dto import Recipe
from main import app  # Assurez-vous d'ajuster l'import selon votre structure de projet

# Utiliser un client de test pour interagir avec l'API
client = TestClient(app)

# Définir des données de test
user_data = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjViNjAyZTBjYTFmNDdhOGViZmQxMTYwNGQ5Y2JmMDZmNGQ0NWY4MmIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbXlhcGktOGEzNDAiLCJhdWQiOiJteWFwaS04YTM0MCIsImF1dGhfdGltZSI6MTcwNjA4Nzc5NSwidXNlcl9pZCI6ImlnVm1VTUNQT1hWQ2pLNGdPWW5HajlXMDh0TDIiLCJzdWIiOiJpZ1ZtVU1DUE9YVkNqSzRnT1luR2o5VzA4dEwyIiwiaWF0IjoxNzA2MDg3Nzk1LCJleHAiOjE3MDYwOTEzOTUsImVtYWlsIjoic3RyaW5nQGhvdG1haWwuZnIiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsic3RyaW5nQGhvdG1haWwuZnIiXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.fRdN4km0U8ZTp0hWdVoL5c0xk0bGHwt_1wVaMhNzdSeIfdaix4U4Dp_Uswnl0hCfQItd8XG-MQAka3y6tnScQ0T8k4hEONacHzF5fJXvvc1pGODtTjq4SxuLI3uoHHyByothqQJLwiVP3LzL6wunvnGC-1DVGdXqFdwJ9DWlE0MyusMGsDzV6jdRJfY9s5sNOBgQ87CCgqwhozXtp8gXi3E3BI0SC5FE6T6VvXR_DYAkEor4QiiiBRladAk-v1uaxRGejjhWzaG00PBCdmNvka0bTMoXnFCw9mK6eXqUfXl19hIaq_6YUH-QNYVm9C9sl_E3J1H5XS4Vxhh-ZSUf5g"}  # Remplacez par un vrai token pour l'utilisateur

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
    response = client.get("/recipes/c58bb370-1054-4ee0-aa1f-b57d2ec39dae", headers=user_data)  # Remplacez par un vrai ID de recette
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Tester l'endpoint de suppression par ID
def test_delete_recipe():
    response = client.delete("/recipes/d95f3750-45c6-4ad3-844e-dc00a79b2ca0", headers=user_data)  # Remplacez par un vrai ID de recette
    assert response.status_code == 200
    assert response.json() == {"message": "recipe deleted"}

# Tester l'endpoint de mise à jour par ID
def test_update_recipe():
    updated_data = {"category": "Updated Category"}
    response = client.patch("/recipes/c58bb370-1054-4ee0-aa1f-b57d2ec39dae", json=updated_data, headers=user_data)  # Remplacez par un vrai ID de recette
    assert response.status_code == 200
    assert response.json() == {"message": "Recipe updated successfully"}
