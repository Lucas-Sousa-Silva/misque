import asyncpg

async def create_postgres_pool():
    connection_settings  = {
        "user":"enem",
        "password":"catapimbas",
        "host":"database",#database é o nome do container.
        "port":5432,
    }
    return await asyncpg.create_pool(**connection_settings)
