import asyncpg

async def create_postgres_pool():
    connection_settings  = {
        "user":"postgres",
        "password":"asdfasdf",
        "port":5432,
    }

    return await asyncpg.create_pool(**connection_settings)
