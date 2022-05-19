from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from starlette.responses import FileResponse

from database.database_connections import create_postgres_pool
from routes.autentication import autentication
from routes.data import data
from routes.test import test

app = FastAPI(
    title="misque - API REST de dados do ENEM",
    description="Uma api de dados abertos acerca de microdados do enem",
    docs_url=None, redoc_url=None, version="0.0.1"
)

###
# # Add the routers from ./backend/routes
###

app.include_router(data)
app.include_router(test)
app.include_router(autentication)

# Add middleware for managing foreign redirects.
# origins = ["http://localhost:8000", "*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/favicon.ico", include_in_schema=False)
async def get_favicon():
    """ Load the favicon from static folder """
    return FileResponse("static/favicon.ico")

###
# # Configure the documentations with some common settings.
###

common_documentations_settings = {
    "openapi_url":"/openapi.json",
    "title":"misque - API REST de dados do ENEM",
}

@app.get("/docs", include_in_schema=False)
def overridden_swagger():
	return get_swagger_ui_html(**common_documentations_settings, swagger_favicon_url="/favicon.ico")

@app.get("/redoc", include_in_schema=False)
def overridden_redoc():
	return get_redoc_html(**common_documentations_settings, redoc_favicon_url="/favicon.ico")


@app.on_event("startup")
async def startup():
    # Adds the posgres pool to internal's state.
    # (Singleton of the pool on the app)
    postgres_pool = await create_postgres_pool()
    setattr(app.state, "pool", postgres_pool)

@app.on_event("shutdown")
async def shutdown():
    pgpool = getattr(app.state, "pool")

    await pgpool.close()
