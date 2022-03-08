import asyncpg

async def create_postgres_pool():
    connection_settings  = {
        "user":"enem",
        "password":"catapimbas",
        "host":"127.0.0.1",
        "port":5432,
    }
    print(connection_settings)
    return await asyncpg.create_pool(**connection_settings)
