from fastapi import FastAPI
from documentations.description import api_description
from documentations.tags import tags_metadata
import routers.router_recipes,routers.router_auth,routers.router_stripe

app = FastAPI(
    title="RecipeBook",
    description=api_description,
    openapi_tags= tags_metadata,
    docs_url='/' 
)
app.include_router(routers.router_auth.router)
app.include_router(routers.router_recipes.router)
app.include_router(routers.router_stripe.router)




