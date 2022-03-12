import asyncpg

async def create_postgres_pool():
    connection_settings  = {
        "user":"enem",
        "password":"catapimbas",
        "host":"192.168.0.108",
        "port":5432,
    }
    print(connection_settings)
    return await asyncpg.create_pool(**connection_settings)
