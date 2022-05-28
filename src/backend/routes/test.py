""" API for """
from typing import List

from asyncpg import Pool
from fastapi import APIRouter, Depends, HTTPException, status

from dependencies.dependencies import get_pool
from models.testingmodels import Conta, ContaComHash, Materia, TesteENEM, TesteMisque, QuestaoENEM
from security.security import get_current_user

test = APIRouter(prefix="/test", tags=["testes"])

###############################################################################
@test.get(
    "/materias",
    response_model=List[Materia]
)
async def get_materias(
    pool:Pool = Depends(get_pool)
):
    QUERY_MATERIAS = "SELECT * FROM MATERIAS;"
    async with pool.acquire() as connection:
        if materias:= await connection.fetch(QUERY_MATERIAS):
            return [Materia(**m) for m in materias]
    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Server can't find table materias")

@test.post("/item-enem", status_code=201)
async def salvar_questao(
    questao: QuestaoENEM,
    user: ContaComHash = Depends(get_current_user),
    pool: Pool = Depends(get_pool)
):
    if user.nick != "poderes_de_grayskull":
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Only with the powers of grayskull you can perform this.")

    QUERY_INSERT_NEW_ITEM_ENEM = """
        INSERT INTO ITEMS_ENEM VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11);
    """
    async with pool.acquire() as connection:
        await connection.execute(
            QUERY_INSERT_NEW_ITEM_ENEM,
            questao.codigo_item,
            questao.enunciado,
            questao.alternativas["A"],
            questao.alternativas["B"],
            questao.alternativas["C"],
            questao.alternativas["D"],
            questao.alternativas["E"],
            questao.resposta,
            questao.habilidade,
            questao.lingua,
            questao.adaptado
        )
    return {'detail':"Successfully created"}

@test.get("/item-enem/{codigo_item}")
async def get_item_by_co_item(codigo_item:int):
    ITEM_QUERY = "SELECT * FROM ITEMS_ENEM WHERE CODIGO_ITEM=$1"
    async with pool.acquire() as connection:
        if item:=await connection.fetchrow(ITEM_QUERY, codigo_item):
            return QuestaoENEM(
                alternativas={
                    "A":item["ALTERNATIVA_A"],
                    "B":item["ALTERNATIVA_B"],
                    "C":item["ALTERNATIVA_C"],
                    "D":item["ALTERNATIVA_D"],
                    "E":item["ALTERNATIVA_E"],
                },
                **item
            )
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"A QuestaoENEM with {codigo_item=} doesn't exists.")
