from fastapi import Request
from database.database_connections import *

async def get_pg_pool(request: Request):
    return getattr(request.app.state, "pool")
