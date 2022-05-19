""" API for """
from typing import List

from asyncpg import Pool
from dependencies.dependencies import get_pool
from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from models.testingmodels import Conta, Materia, TesteENEM, TesteMisque

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

# @test.get(
#     "/testes",
#     response_model=TesteMisque
# )
# async def get_testes(
#     conta_atual: get_
# ):

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


