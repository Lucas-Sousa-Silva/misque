""" Here we make some account handler functions about the accounts that we are going to manage. """
from asyncpg import Connection
from models.testingmodels import Conta

async def conta_exists(connection: Connection, user: Conta):
    return bool(await connection.fetchrow("""
        SELECT NICK FROM CONTAS WHERE NICK=$1;
    """, user.nome))

async def create_conta(connection: Connection, conta: Conta, hashed_password:str):
    # conta already exists
    if conta_exists(conta):
        raise ValueError("This conta already exists in the database.")
    # else insert into contas values as bellow
    await connection.execute(
    """
        INSERT INTO CONTAS VALUES($1,$2,$3)
    """,
        conta.nick,
        conta.nascimento,
        hashed_password
    )

async def delete_conta(connection:Connection, conta:Conta, hashed_password:str):
    if not counta_exists(conta):
        raise ValueError("This conta don't exists in the database.")
    await connection.execute(
    """
        DELETE FROM CONTAS
        WHERE NICK=$1, NASCIMENTO=$2, SENHA=$3;
    """,
        conta.nick,
        conta.nascimento,
        hashed_password
    )
