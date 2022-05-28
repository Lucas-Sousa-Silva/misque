import uuid
from datetime import date, datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, ValidationError, validator

# Usable regexes
regex_nick  = r"[a-zA-Z0-9_-]*"
regex_senha = r"[0-9a-z]*"

class Conta(BaseModel):

    nick: str = Field(description="Nick da conta", min_length=6, max_length=20, regex=regex_nick)
    nascimento: date = Field(description="Nascimento do usuário")

class ContaComHash(Conta):

    hashed_password:str = Field()


class Materia(BaseModel):

    nome: str = Field(description="Nome da matéria ou área do conhecimento")
    codigo: str = Field(description="Código da matéria.", min_length=2, max_length=2) 


class Questao(BaseModel):

    enunciado: str = Field(description="Comando da questão")
    alternativas: Dict[str, str] = Field(
        default = {'A':None,'B':None,'C':None,'D':None,'E':None,},
        description = "Alternativas da questão, deve conter alternativas",
    )
    resposta: Optional[str] = Field(description="Caso configurada mostra qual a resposta da questão.")

class QuestaoENEM(Questao):

    codigo_item: int = Field(description="Código interno do enem. Ou caso for de um ano esotérico, é customizado")
    habilidade:int = Field(description="Mostra o nível de habilidade para responder á esta questão.")
    lingua: bool | None = Field(description="Se é inglês é True, se é espanhol é False, se não é null.")
    adaptado: bool | None = Field(description="Se é adaptado ou não. Pode ser nulo")

class TesteENEM(BaseModel):
    codigo_prova: int = Field(description="Codigo identificador da")
    materia: Materia = Field(description="Matéria que essa prova usa")


class TesteENEM(BaseModel):

    ano: int = Field(description="Ano da prova do enem")
    cor: str = Field(description="Cor da prova")
    reaplicacao: bool = Field(description="Campo descreve se esta prova é uma reaplicação")


class TesteMisque(BaseModel):

    participante: Conta = Field(description="Conta de quem quis fazer a prova")
    criado: datetime = Field(description="Momento em que o teste foi criado")
    iniciado: datetime | None = Field(description="Momento em que o teste foi iniciado")
    concluido: datetime | None = Field(description="Momento em que o teste foi concluido")
