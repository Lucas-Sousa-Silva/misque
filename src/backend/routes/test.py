""" API for """
from fastapi import APIRouter, Body, Path, Depends, HTTPException, status
from asyncpg import Pool
from typing import List

from dependencies.dependencies import get_pool

from models.testingmodels import (
    Materia,
    TesteENEM,
)

test = APIRouter(prefix="/test", tags=["testes"])

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
    if materia:=[*filter(lambda mat: mat.codigo==co_materia,materias)]:
        return materia
    raise HTTPException(status.HTTP_404_NOT_FOUND, f"A materia with {co_materia=} can't be found.")

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



