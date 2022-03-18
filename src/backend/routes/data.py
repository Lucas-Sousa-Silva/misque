from fastapi import APIRouter, Depends
from typing import List

from models.basemodels import Estado, Municipio
from dependencies.dependencies import get_pg_pool
from asyncpg import Pool

data = APIRouter()

################################################################################

@data.get(
    "/estados",
    description="Retorna todos os estados.",
    response_model=List[Estado],
)
async def get_estados(
    pool: Pool = Depends(get_pg_pool)
) -> List[Estado]:
    QUERY_ESTADOS ="""
        SELECT * FROM ESTADOS;
    """
    async with pool.acquire() as conn:
        return [
            Estado(**estado)
            for estado in await conn.fetch(QUERY_ESTADOS)
        ]

# @data.get("/estados/{co_uf}")
# async def get_estado(
#     co_uf: int
# ):
#     return 


@data.get(
    "/municipios",
    description="Retorna todos os municipios existentes.(Pode demorar)",
    response_model=List[Municipio],
)
async def get_municipios(
    pool: Pool = Depends(get_pg_pool)
):
    QUERY_MUNICIPIOS="""
        SELECT * FROM MUNICIPIOS;
    """
    muns = []
    async with pool.acquire() as conn:
        for m in await conn.fetch(QUERY_MUNICIPIOS):
            muns.append(Municipio(**m))
    return muns
        


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