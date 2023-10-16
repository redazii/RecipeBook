# Import du framework
from fastapi import FastAPI

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata

#Routers
import routers.router_recipes
# Initialisation de l'API
app = FastAPI(
    title="API",
    description=api_description,
    openapi_tags= tags_metadata
)

# Router dédié aux recettes
app.include_router(routers.router_recipes.router)
