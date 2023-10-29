from fastapi import FastAPI
from documentations.description import api_description
from documentations.tags import tags_metadata
import routers.router_recipes

app = FastAPI(
    title="RecipeBook",
    description=api_description,
    openapi_tags= tags_metadata,
    docs_url='/' 
)
app.include_router(routers.router_recipes.router)





