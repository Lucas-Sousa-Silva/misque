from asyncpg import Pool

from fastapi import APIRouter, Depends, HTTPException, status

from typing import List
from dependencies.dependencies import get_pool
from models.basemodels import (
    AtendimentoEeE,
    AtendimentoEspecializado,
    AtendimentoEspecifico,
    Escola,
    Estado,
    Municipio,
    Participante,
)
from routes.autentication import oauth2_scheme
data = APIRouter(tags=['data'],prefix="/data",)


################################################################################
@data.get(
    "/estados",
    response_model=List[Estado],
)
async def get_estados(
    pool: Pool = Depends(get_pool),
) -> List[Estado]:
    """ Retorna todos os estados. """
    QUERY_ESTADOS = """
        SELECT
            *
        FROM ESTADOS;
    """
    async with pool.acquire() as conn:
        if estados:= [Estado(**e) for e in await conn.fetch(QUERY_ESTADOS)]:
            return estados


################################################################################
@data.get(
    "/estados/{co_uf}",
    response_model=List[Estado],
)
async def get_estado_por_codigo(
    co_uf: int,
    pool: Pool = Depends(get_pool),
)->List[Estado]:
    """Retorna todos os municipios de um certo estado."""
    QUERY_MUNICIPIOS = """
        SELECT
            *
        FROM ESTADOS
        WHERE
            CO_UF=$1;
    """
    async with pool.acquire() as conn:
        if estados:= [Estado(**m) for m in await conn.fetch(QUERY_MUNICIPIOS, co_uf)]:
            return estados
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Estado com código {co_uf=} não existe.")


################################################################################
@data.get(
    "/estados/{co_uf}/municipios",
    response_model=List[Municipio],
)
async def get_municipios_por_estado(
    co_uf: int,
    pool: Pool = Depends(get_pool),
)->List[Municipio]:
    """Retorna todos os municipios de um certo estado."""
    QUERY_MUNICIPIOS = """
        SELECT
            *
        FROM MUNICIPIOS
        WHERE
            CO_UF_ESTADO=$1;
    """
    async with pool.acquire() as conn:
        if municipios:= [
            Municipio(**m) for m in await conn.fetch(QUERY_MUNICIPIOS, co_uf)
        ]:
            return municipios
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Municipios com código {co_uf=} não existe.")


################################################################################
@data.get(
    "/estados/{co_uf}/municipios/{co_municipio}",
    response_model=List[Municipio],
)
async def get_municipio_por_codigo_uf_e_co_municipio(
    co_uf: int,
    co_municipio:int,
    pool: Pool = Depends(get_pool),
)->List[Municipio]:
    """Retorna o municipio especificado pelo <strong>co_uf_estado</strong> e <strong>co_municipio</strong>."""
    QUERY_MUNICIPIO = """
        SELECT
            *
        FROM MUNICIPIOS
        WHERE
            CO_UF_ESTADO=$1 AND
            CO_MUNICIPIO=$2;
    """
    async with pool.acquire() as conn:
        if municipios:= [
            Municipio(**m)
            for m in await conn.fetch(QUERY_MUNICIPIO, co_uf, co_municipio)
        ]:
            return municipios
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Municipio com código {co_uf=} e {co_municipio=} não existe.")


################################################################################
@data.get(
    "/estados/{co_uf}/municipios/{co_municipio}/escolas",
    response_model=List[Escola],
)
async def get_escolas_por_co_municipio_co_uf_estado(
    co_uf: int,
    co_municipio:int,
    pool: Pool = Depends(get_pool),
)->List[Municipio]:
    """Retorna o municipio especificado pelo <strong>co_uf_estado</strong> e <strong>co_municipio</strong>."""
    QUERY_MUNICIPIOS = """
        SELECT
            *
        FROM ESCOLAS
        WHERE
            CO_MUNICIPIO_ESC IN (
                SELECT
                    CO_MUNICIPIO
                FROM MUNICIPIOS
                WHERE CO_UF_ESTADO=$1 AND
                CO_MUNICIPIO=$2
            );
    """
    async with pool.acquire() as conn:
        if escolas :=await conn.fetch(QUERY_MUNICIPIOS,co_uf, co_municipio,):
            return [Escola(**e) for e in escolas]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Escola não encontrada.")


# ################################################################################
# @data.get(
#     "/escolas",
#     response_model=List[Escola],
# )
# async def get_escolas(
#     pool:Pool = Depends(get_pool)
# ):
#     """ Retorna todas as escolas que estão no banco de dados. """
#     QUERY_ESCOLAS = """
#         SELECT
#             CO_ESCOLA,
#             TP_DEPENDENCIA_ADM_ESC,
#             TP_LOCALIZACAO_ESC,
#             TP_SIT_FUNC_ESC
#         FROM ESCOLAS;
#     """
#     async with pool.acquire() as conn:
#         return [
#             Escola(**e)
#             for e in await conn.fetch(QUERY_ESCOLAS)
#         ]


# @data.get(
#     "/participantes",
#     response_model=List[Participante]
# )
# async def get_participantes(
#     pool:Pool = Depends(get_pool),
# )->List[Participante]:
#     """
#     Aqui se faz uma query na tabela principal do banco de dados. A tabela de
#     participantes. A mesma é enorme e não pode ser executada pelo /docs.
#     Cuidado. Esta demora muito.
#     """
#     QUERY_PARTICIPANTES="""
#         SELECT * FROM PARTICIPANTES;
#     """
#     async with pool.acquire() as conn:
#         return [
#             Participante(**p)
#             for p in await conn.fetch(QUERY_PARTICIPANTES)
#         ]


# # @data.get("/municipios/{co_municipio}/escolas")
# # async def get_escolas_by_municipio(
# #     co_municipio:int
# # ):
# #     return 

# @data.get("/municipios/{co_municipio}/escolas/{co_escola}")
# async def get_escola(
#     co_municipio:int,
#     co_escola:int
# ):
#     return 
# @data.get("/escolas")
# async def get_escolas(
#     co_municipio: Optional[int],
#     co_estado: Optional[int]
# ):
#     return 

# ################################################################################

# @data.get("/inscrito/{numero}")
# async def get_inscrito(
#     numero: int,
#     _usuario_atual: User = Depends(inscrito),
# ):
#     return 
