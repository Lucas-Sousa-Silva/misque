from fastapi import FastAPI
from routes.data import data
from database.database_connections import create_postgres_pool
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from starlette.responses import FileResponse
origins = ["http://localhost:8000", "*"]

app = FastAPI(
    title="misque - API REST de dados do ENEM",
    description="Uma api de dados abertos acerca de microdados do enem",
    docs_url=None, redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/favicon.ico", include_in_schema=False)
async def get_favicon():
    return FileResponse("static/favicon.ico")

@app.get("/docs", include_in_schema=False)
def overridden_swagger():
	return get_swagger_ui_html(openapi_url="/openapi.json", title="misque - API REST de dados do ENEM", swagger_favicon_url="/favicon.ico")

@app.get("/redoc", include_in_schema=False)
def overridden_redoc():
	return get_redoc_html(openapi_url="/openapi.json", title="misque - API REST de dados do ENEM", redoc_favicon_url="/favicon.ico")






#app.add_route("/data", data)
app.include_router(data)
@app.on_event("startup")
async def startup():
    # Principalmente faz injeção de dependência iniciais.
    # Adiciona a pool do postgres a ser acessível a todos os endpoints.
    postgres_pool = await create_postgres_pool()
    setattr(app.state, "pool", postgres_pool)
