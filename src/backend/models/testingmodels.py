import re, uuid, traceback
from pydantic import BaseModel, Field, validator, ValidationError
from typing import List, Optional, Union, Set, Dict
from datetime import date

regex_nick = r"[0-9a-z]*"
regex_senha = r"[0-9a-z]*"


class Conta(BaseModel):

    nick: str = Field(description="Nick da conta", min_length=6, max_length=15, regex=regex_nick)
    nascimento: date = Field(description="Nascimento do usuário")

class Questao(BaseModel):

    identidade: uuid.UUID = Field(description="UUID da questão. Deve ser única no universo.", const=True)
    ano: Optional[int] = Field(description="Ano em que essa questão caiu no ENEM.")
    comando: str = Field(description="Comando da questão")
    alternativas: Dict[str, str] = Field(
        default = {'A':None,'B':None,'C':None,'D':None,'E':None,},
        description = "Alternativas da questão, deve conter alternativas",
        min_length = 5,
        max_length = 5,
    )

class Materia(BaseModel):
    nome: str = Field(description="Nome da matéria ou área do conhecimento")
    codigo: str = Field(description="Código da matéria.", min_length=2, max_length=2) 

class Gabarito(BaseModel):

    respostas : Dict[Questao, str] = Field(description="Mapa de respostas do usuário.")


class Teste(BaseModel):
    materia: Materia = Field(description="Matéria que essa prova usa")
    questoes: List[Questao] = Field(description="Todas as questões do ano dessa prova.")

class ProvaENEM(Teste):
    ano: int = Field(description="Ano da prova do enem")
    cor: str = Field(description="Cor da prova")

class TesteMisque(BaseModel):

    participante: Conta = Field(description="Conta de quem quis fazer a prova")
    materia: str = Field(description="Materia")
    questoes: List[Questao] = Field(description="Questões")
    respostas : Dict[Questao, str] = Field(description="Mapa de respostas do usuário.")


