from fastapi import FastAPI
from routes.data import data
from database.database_connections import create_postgres_pool
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:8000", "*"]

app = FastAPI(
    title="misque - API REST de dados do ENEM",
    description="Uma api de dados abertos acerca de microdados do enem",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.add_route("/data", data)
app.include_router(data, tags=['data'])
@app.on_event("startup")
async def startup():
    # Principalmente faz injeção de dependência iniciais.
    # Adiciona a pool do postgres a ser acessível a todos os endpoints.
    postgres_pool = await create_postgres_pool()
    setattr(app.state, "pool", postgres_pool)
