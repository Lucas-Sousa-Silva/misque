#from dataclasses import dataclass
from pydantic import BaseModel
from typing import List, Optional, Union
from enum import Enum

class Estado(BaseModel):
    co_uf: int
    sg_uf: str

class Municipio(BaseModel):
    codigo:int
    nome:str

class Participante(BaseModel):
    inscricao: int
    ano_enem: int
    idade: int
    sexo: int
    estado_civil: int
    cor: int
    situacao_conclusao : str
    ano_conclusao : int
    treineiro: bool

class Escola(BaseModel):
    codigo: int
    dependencia : int
    localizacao : int
    situacao_funcionamento : int

class AtendimentoEspecializado(BaseModel):
    baixa_visao:bool
    cegueira:bool
    surdez:bool
    deficiencia_auditiva:bool
    surdo_cegueira:bool
    deficiencia_fisica:bool
    deficiencia_mental:bool
    deficit_atencao:bool
    dislexia:bool
    discalculia:bool
    autismo:bool
    visao_monocular:bool
    outra_def:bool

class AtendimentoEspecifico(BaseModel):
    gestante: bool
    lactante: bool
    idoso: bool
    estuda_classe_hospitalar: bool

class AtendimentoEeE(BaseModel):
    sem_recurso: bool
    braille: bool
    ampliada_24: bool
    ampliada_18: bool
    ledor: bool
    acesso: bool
    transcricao: bool
    libras: bool
    tempo_adicional: bool
    leitura_labial: bool
    mesa_cadeira_rodas: bool
    mesa_cadeira_separada: bool
    apoio_perna: bool
    guia_interprete: bool
    computador: bool
    cadeira_especial: bool
    cadeira_canhoto: bool
    cadeira_acolchoada: bool
    prova_deitado: bool
    mobiliario_obeso: bool
    lamina_overlay: bool
    protetor_auricular: bool
    medidor_glicose: bool
    maquina_braile: bool
    soroban: bool
    marca_passo: bool
    sonda: bool
    medicamentos: bool
    sala_individual: bool
    sala_especial: bool
    sala_acompanhante: bool
    mobiliario_especifico: bool
    material_especifico: bool
    nome_social: bool

class DadosProvaObjetiva(BaseModel):
    presenca_cn: int
    presenca_ch: int
    presenca_lc: int
    presenca_mt: int
    prova_cn: int
    prova_ch: int
    prova_lc: int
    prova_mt: int
    nu_nota_cn: int
    nu_nota_ch: int
    nu_nota_lc: int
    nu_nota_mt: int
    tp_lingua : bool

class DadosRedacao(BaseModel):
    status_redacao: int 
    nota_comp1:int
    nota_comp2:int
    nota_comp3:int
    nota_comp4:int
    nota_comp5:int
    nota_redacao:int

class RespostasQuestionario(BaseModel):
    Q001 :str
    Q002 :str
    Q003 :str
    Q004 :str
    Q005 :str
    Q006 :str
    Q007 :str
    Q008 :str
    Q009 :str
    Q010 :str
    Q011 :str
    Q012 :str
    Q013 :str
    Q014 :str
    Q015 :str
    Q016 :str
    Q017 :str
    Q018 :str
    Q019 :str
    Q020 :str
    Q021 :str
    Q022 :str
    Q023 :str
    Q024 :str
    Q025 :str
