import uuid

from typing import List, Dict, Optional
from pydantic import BaseModel, Field, validator, ValidationError
from datetime import date, datetime

# Usable regexes
regex_nick  = r"[0-9a-z]*"
regex_senha = r"[0-9a-z]*"

class Conta(BaseModel):

    nick: str = Field(description="Nick da conta", min_length=6, max_length=15, regex=regex_nick)
    nascimento: date = Field(description="Nascimento do usuário")


class Questao(BaseModel):

    identidade: uuid.UUID = Field(description="UUID da questão. Deve ser única no universo.", const=True)
    comando: str = Field(description="Comando da questão")
    alternativas: Dict[str, str] = Field(
        default = {'A':None,'B':None,'C':None,'D':None,'E':None,},
        description = "Alternativas da questão, deve conter alternativas",
        min_length = 5,
        max_length = 5,
    )
    resposta: Optional[str] = Field(description="Caso configurada mostra qual a resposta da questão.")


class Materia(BaseModel):

    nome: str = Field(description="Nome da matéria ou área do conhecimento")
    codigo: str = Field(description="Código da matéria.", min_length=2, max_length=2) 


class Teste(BaseModel):

    materia: Materia = Field(description="Matéria que essa prova usa")
    questoes: List[Questao] = Field(description="Todas as questões do ano desse teste.")


class TesteENEM(Teste):

    ano: int = Field(description="Ano da prova do enem")
    cor: str = Field(description="Cor da prova")
    reaplicacao: bool = Field(description="Campo descreve se esta prova é uma reaplicação")


class TesteMisque(Teste):

    participante: Conta = Field(description="Conta de quem quis fazer a prova")
    criado: datetime = Field(description="Momento em que o teste foi criado")
    iniciado: datetime | None = Field(description="Momento em que o teste foi iniciado")
    concluido: datetime | None = Field(description="Momento em que o teste foi concluido")
