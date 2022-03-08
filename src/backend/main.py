from fastapi import FastAPI
from routes.data import data
from database.database_connections import create_postgres_pool

app = FastAPI()

app.add_route("/data", data)

@app.on_event("startup")
async def startup():
    # Mainly makes initial dependency injections

    # Add postgres pool to be accessible to all endpoints
    postgres_pool = await create_postgres_pool()
    setattr(app.state, "pool", postgres_pool)
