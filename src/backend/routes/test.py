from fastapi import APIRouter, Body, Path, Depends
from asyncpg import Pool
from typing import List
from dependencies.dependencies import get_pool
from models.testingmodels import (
    Materia,
    ProvaENEM,
)
test = APIRouter(prefix="/test")

materias = [
    Materia(
        nome="Ciências da Natureza",
        codigo="CN",
    ),
    Materia(
        nome="Ciências Humanas",
        codigo="CH",
    ),
    Materia(
        nome="Linguagens e Códigos",
        codigo="LC",
    ),
    Materia(
        nome="Matemática",
        codigo="MT",
    ),
]

###############################################################################
@test.get(
    "/materias",
    response_model=List[Materia]
)
async def get_materias():
    return materias

###############################################################################
@test.get(
    "/materias/{co_materia}",
    response_model=List[Materia],
)
async def get_materias(
    co_materia: str,
    pool: Pool = Depends(get_pool),
):
    return [*filter(lambda mat: mat.codigo==co_materia,materias)]

# ###############################################################################
# @test.get(
#     "/materias/{co_materia}/provas",
#     response_model=List[ProvaENEM],
# )
# async def get_materias(
#     co_materia: str,
#     pool: Pool = Depends(get_pool),
# ):
#     return [*filter(lambda mat: mat.codigo==co_materia,materias)]




# @test.post("/contas")
# async def get_testes(
#     body: Body = Body(),
#     pool: Pool = Depends(get_pool),
#     _conta: Conta = Depends(conta)
# ):
#     async with pool.acquire() as connection:
#         testes_realizados = await get_testes(usuario)



