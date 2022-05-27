--    ____ ___  (_)________ ___  _____ 
--   / __ `__ \/ / ___/ __ `/ / / / _ \
--  / / / / / / (__  ) /_/ / /_/ /  __/
-- /_/ /_/ /_/_/____/\__, /\__,_/\___/ 
--                     /_/             
-- Copyright (C) 2022  Lucas Sousa Silva

-- This program is free software: you can redistribute it and/or modify
-- it under the terms of the GNU General Public License as published by
-- the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.

-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.

-- You should have received a copy of the GNU General Public License
-- along with this program.  If not, see <https://www.gnu.org/licenses/>.

-------------------------------------------------------------------------------
---------- TABELAS REALATIVAS Á DADOS SALVOS DOS MICRODADOS DO ENEM -----------
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS ESTADOS (
    CO_UF                       SMALLINT NOT NULL PRIMARY KEY,
    SG_UF                       VARCHAR(2) NOT NULL UNIQUE
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS MUNICIPIOS (
    CO_MUNICIPIO                INTEGER NOT NULL PRIMARY KEY,
    CO_UF_ESTADO                SMALLINT REFERENCES ESTADOS(CO_UF),
    NO_MUNICIPIO                VARCHAR(150) NOT NULL 
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ITENS_PROVA  (
    -- DADOS DA PROVA --
    CO_POSICAO                  SMALLINT NOT NULL,
    SG_AREA                     VARCHAR(2) NOT NULL,
    CO_ITEM                     INTEGER NOT NULL,
    TX_GABARITO                 CHAR NOT NULL,
    CO_HABILIDADE               SMALLINT NOT NULL,
    TX_COR                      VARCHAR(7) NOT NULL,
    CO_PROVA                    SMALLINT NOT NULL,
    TP_LINGUA                   BOOLEAN NOT NULL,
    IN_ITEM_ADAPTADO            BOOLEAN NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ESCOLAS (
    CO_ESCOLA                   INTEGER NOT NULL PRIMARY KEY,

    -- FKS DA TABELA DE MUNICIPIOS --
    CO_MUNICIPIO_ESC            INTEGER REFERENCES MUNICIPIOS(CO_MUNICIPIO),
    TP_ESCOLA                   SMALLINT NOT NULL,
    TP_DEPENDENCIA_ADM_ESC      SMALLINT NOT NULL,
    TP_LOCALIZACAO_ESC          VARCHAR(6) NOT NULL,
    TP_SIT_FUNC_ESC             SMALLINT NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS PARTICIPANTES (
    -- DADOS DO PARTICIPANTE --
    NU_INSCRICAO                BIGINT NOT NULL PRIMARY KEY,
    NU_ANO                      SMALLINT NOT NULL,
    
    NU_IDADE                    SMALLINT NOT NULL,
    TP_SEXO                     BOOLEAN NOT NULL ,
    TP_ESTADO_CIVIL             SMALLINT NOT NULL ,
    TP_COR_RACA                 SMALLINT NOT NULL ,
    TP_NACIONALIDADE            SMALLINT NOT NULL ,

    TP_ST_CONCLUSAO             SMALLINT NOT NULL,
    TP_ANO_CONCLUIU             SMALLINT NOT NULL,

    TP_ENSINO                   SMALLINT NOT NULL,
    IN_TREINEIRO                BOOLEAN NOT NULl
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS APLICACOES_DE_PROVAS (
    -- FK DA TABELA DE PARTICIPANTES --
    NU_INSCRICAO                BIGINT UNIQUE REFERENCES PARTICIPANTES(NU_INSCRICAO),
    -- FKS DA TABELA DE MUNICIPIOS --
    CO_MUNICIPIO_PROVA          INTEGER REFERENCES MUNICIPIOS(CO_MUNICIPIO)
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS NASCIMENTOS_DE_PARTICIPANTES(
    -- FK DA TABELA DE PARTICIPANTES --
    NU_INSCRICAO                BIGINT UNIQUE REFERENCES PARTICIPANTES(NU_INSCRICAO),
    -- FKS DA TABELA DE MUNICIPIOS --
    CO_MUNICIPIO_NASCIMENTO     INTEGER REFERENCES MUNICIPIOS(CO_MUNICIPIO)
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS RESIDENCIA_DE_PARTICIPANTES(
    -- FK DA TABELA DE PARTICIPANTES --
    NU_INSCRICAO                BIGINT UNIQUE REFERENCES PARTICIPANTES(NU_INSCRICAO),
    -- FKS DA TABELA DE MUNICIPIOS --
    CO_MUNICIPIO_RESIDENCIA     INTEGER REFERENCES MUNICIPIOS(CO_MUNICIPIO)
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ESCOLAS_DOS_PARTICIPANTES(
    -- FK DA TABELA DE PARTICIPANTES --
    NU_INSCRICAO                BIGINT UNIQUE REFERENCES PARTICIPANTES(NU_INSCRICAO),
    -- FKS DA TABELA DE ESCOLAS --
    CO_ESCOLA_ESTUDA            INTEGER REFERENCES ESCOLAS(CO_ESCOLA)
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS DADOS_DA_PROVA_OBJETIVA (
    -- FK DA TABELA DE PARTICIPANTES --
    NU_INSCRICAO                BIGINT UNIQUE REFERENCES PARTICIPANTES(NU_INSCRICAO),

    -- DADOS DA PROVA OBJETIVA -- 
    TP_PRESENCA_CN              SMALLINT NOT NULL,
    TP_PRESENCA_CH              SMALLINT NOT NULL,
    TP_PRESENCA_LC              SMALLINT NOT NULL,
    TP_PRESENCA_MT              SMALLINT NOT NULL,
    CO_PROVA_CN                 SMALLINT NOT NULL,
    CO_PROVA_CH                 SMALLINT NOT NULL,
    CO_PROVA_LC                 SMALLINT NOT NULL,
    CO_PROVA_MT                 SMALLINT NOT NULL,
    NU_NOTA_CN                  REAL NOT NULL,
    NU_NOTA_CH                  REAL NOT NULL,
    NU_NOTA_LC                  REAL NOT NULL,
    NU_NOTA_MT                  REAL NOT NULL,
    TX_RESPOSTAS_CN             CHAR[45]  NOT NULL,
    TX_RESPOSTAS_CH             CHAR[45]  NOT NULL,
    TX_RESPOSTAS_LC             CHAR[45]  NOT NULL,
    TX_RESPOSTAS_MT             CHAR[45]  NOT NULL,
    TP_LINGUA                   BOOLEAN NOT NULL,
    TX_GABARITO_CN              CHAR[45]  NOT NULL,
    TX_GABARITO_CH              CHAR[45]  NOT NULL,
    TX_GABARITO_LC              CHAR[45]  NOT NULL,
    TX_GABARITO_MT              CHAR[45]  NOT NULL
);

------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ATENDIMENTO_ESPECIALIZADOS (
    -- FK DA TABELA DE PARTICIPANTES --
    NU_INSCRICAO                BIGINT UNIQUE REFERENCES PARTICIPANTES(NU_INSCRICAO),

    -- DADOS DOS PEDIDOS DE ATENDIMENTO ESPECIALIZADO  --
    IN_BAIXA_VISAO              BOOLEAN NOT NULL,
    IN_CEGUEIRA                 BOOLEAN NOT NULL,
    IN_SURDEZ                   BOOLEAN NOT NULL,
    IN_DEFICIENCIA_AUDITIVA     BOOLEAN NOT NULL,
    IN_SURDO_CEGUEIRA           BOOLEAN NOT NULL,
    IN_DEFICIENCIA_FISICA       BOOLEAN NOT NULL,
    IN_DEFICIENCIA_MENTAL       BOOLEAN NOT NULL,
    IN_DEFICIT_ATENCAO          BOOLEAN NOT NULL,
    IN_DISLEXIA                 BOOLEAN NOT NULL,
    IN_DISCALCULIA              BOOLEAN NOT NULL,
    IN_AUTISMO                  BOOLEAN NOT NULL,
    IN_VISAO_MONOCULAR          BOOLEAN NOT NULL,
    IN_OUTRA_DEF                BOOLEAN NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ATENDIMENTO_ESPECIFICOS (
    -- FK DA TABELA DE PARTICIPANTES --
    NU_INSCRICAO                BIGINT UNIQUE REFERENCES PARTICIPANTES(NU_INSCRICAO),


    -- DADOS DOS PEDIDOS DE ATENDIMENTO ESPECÍFICO --
    IN_GESTANTE                 BOOLEAN NOT NULL,
    IN_LACTANTE                 BOOLEAN NOT NULL,
    IN_IDOSO                    BOOLEAN NOT NULL,
    IN_ESTUDA_CLASSE_HOSPITALAR BOOLEAN NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ATENDIMENTO_ESPECIALIZADO_E_ESPECIFICOS (
    -- FK DA TABELA DE PARTICIPANTES --
    NU_INSCRICAO                BIGINT UNIQUE REFERENCES PARTICIPANTES(NU_INSCRICAO),

    IN_SEM_RECURSO              BOOLEAN NOT NULL,
    IN_BRAILLE                  BOOLEAN NOT NULL,
    IN_AMPLIADA_24              BOOLEAN NOT NULL,
    IN_AMPLIADA_18              BOOLEAN NOT NULL,
    IN_LEDOR                    BOOLEAN NOT NULL,
    IN_ACESSO                   BOOLEAN NOT NULL,
    IN_TRANSCRICAO              BOOLEAN NOT NULL,
    IN_LIBRAS                   BOOLEAN NOT NULL,
    IN_TEMPO_ADICIONAL          BOOLEAN NOT NULL,
    IN_LEITURA_LABIAL           BOOLEAN NOT NULL,
    IN_MESA_CADEIRA_RODAS       BOOLEAN NOT NULL,
    IN_MESA_CADEIRA_SEPARADA    BOOLEAN NOT NULL,
    IN_APOIO_PERNA              BOOLEAN NOT NULL,
    IN_GUIA_INTERPRETE          BOOLEAN NOT NULL,
    IN_COMPUTADOR               BOOLEAN NOT NULL,
    IN_CADEIRA_ESPECIAL         BOOLEAN NOT NULL,
    IN_CADEIRA_CANHOTO          BOOLEAN NOT NULL,
    IN_CADEIRA_ACOLCHOADA       BOOLEAN NOT NULL,
    IN_PROVA_DEITADO            BOOLEAN NOT NULL,
    IN_MOBILIARIO_OBESO         BOOLEAN NOT NULL,
    IN_LAMINA_OVERLAY           BOOLEAN NOT NULL,
    IN_PROTETOR_AURICULAR       BOOLEAN NOT NULL,
    IN_MEDIDOR_GLICOSE          BOOLEAN NOT NULL,
    IN_MAQUINA_BRAILE           BOOLEAN NOT NULL,
    IN_SOROBAN                  BOOLEAN NOT NULL,
    IN_MARCA_PASSO              BOOLEAN NOT NULL,
    IN_SONDA                    BOOLEAN NOT NULL,
    IN_MEDICAMENTOS             BOOLEAN NOT NULL,
    IN_SALA_INDIVIDUAL          BOOLEAN NOT NULL,
    IN_SALA_ESPECIAL            BOOLEAN NOT NULL,
    IN_SALA_ACOMPANHANTE        BOOLEAN NOT NULL,
    IN_MOBILIARIO_ESPECIFICO    BOOLEAN NOT NULL,
    IN_MATERIAL_ESPECIFICO      BOOLEAN NOT NULL,
    IN_NOME_SOCIAL              BOOLEAN NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS DADOS_DA_REDACAO (
    -- FK DA TABELA DE PARTICIPANTES --
    NU_INSCRICAO                BIGINT UNIQUE REFERENCES PARTICIPANTES(NU_INSCRICAO),

    -- DADOS DA REDAÇÃO --
    TP_STATUS_REDACAO           SMALLINT NOT NULL,
    NU_NOTA_COMP1               SMALLINT NOT NULL,
    NU_NOTA_COMP2               SMALLINT NOT NULL,
    NU_NOTA_COMP3               SMALLINT NOT NULL,
    NU_NOTA_COMP4               SMALLINT NOT NULL,
    NU_NOTA_COMP5               SMALLINT NOT NULL,
    NU_NOTA_REDACAO             SMALLINT NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS QUESTIONARIO_SOCIOECONOMICO (
    -- FK DA TABELA DE PARTICIPANTES --
    NU_INSCRICAO                BIGINT UNIQUE REFERENCES PARTICIPANTES(NU_INSCRICAO),

    -- DADOS DO QUESTIONÁRIO SOCIOECONÔMICO --
    Q001                        CHAR NOT NULL,
    Q002                        CHAR NOT NULL,
    Q003                        CHAR NOT NULL,
    Q004                        CHAR NOT NULL,
    Q005                        SMALLINT NOT NULL,
    Q006                        CHAR NOT NULL,
    Q007                        CHAR NOT NULL,
    Q008                        CHAR NOT NULL,
    Q009                        CHAR NOT NULL,
    Q010                        CHAR NOT NULL,
    Q011                        CHAR NOT NULL,
    Q012                        CHAR NOT NULL,
    Q013                        CHAR NOT NULL,
    Q014                        CHAR NOT NULL,
    Q015                        CHAR NOT NULL,
    Q016                        CHAR NOT NULL,
    Q017                        CHAR NOT NULL,
    Q018                        CHAR NOT NULL,
    Q019                        CHAR NOT NULL,
    Q020                        CHAR NOT NULL,
    Q021                        CHAR NOT NULL,
    Q022                        CHAR NOT NULL,
    Q023                        CHAR NOT NULL,
    Q024                        CHAR NOT NULL,
    Q025                        CHAR NOT NULL
);

-------------------------------------------------------------------------------
--- TABELAS REALATIVAS Á DADOS SALVOS DOS TESTES MISQUE E QUESTÕES DO ENEM ----
-------------------------------------------------------------------------------


-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS MATERIAS(
    CODIGO                      VARCHAR(2) NOT NULL UNIQUE PRIMARY KEY,
    NOME                        VARCHAR(50) NOT NULL UNIQUE
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS CONTAS(
    NICK                        VARCHAR(20) NOT NULL CHECK(LENGTH(NICK) > 6) PRIMARY KEY,
    NASCIMENTO                  DATE NOT NULL,
    SENHA_HASH                  TEXT
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS TESTES_ENEM(
    -- CÓDIGO INTERNO DO ENEM --
    CODIGO_PROVA                SMALLINT NOT NULL PRIMARY KEY,

    -- FK DA TABELA DE MATERIAS --
    CODIGO_MATERIA              VARCHAR(2) REFERENCES MATERIAS(CODIGO),
    COR                         VARCHAR(15),
    ANO                         SMALLINT NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ITEMS_ENEM(
    CODIGO_ITEM                 INTEGER NOT NULL PRIMARY KEY,
    ENUNCIADO                   TEXT NOT NULL,
    ALTERNATIVA_A               TEXT NOT NULL,
    ALTERNATIVA_B               TEXT NOT NULL,
    ALTERNATIVA_C               TEXT NOT NULL,
    ALTERNATIVA_D               TEXT NOT NULL,
    ALTERNATIVA_E               TEXT NOT NULL,
    RESPOSTA                    CHAR NOT NULL,
    HABILIDADE                  SMALLINT NOT NULL,
    LINGUA                      BOOLEAN,
    ADAPTADO                    BOOLEAN
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS QUESTOES_ENEM(
    -- FK DA TABELA ITEMS --
    CODIGO_ITEM                 INTEGER REFERENCES ITEMS_ENEM(CODIGO_ITEM),
    CODIGO_PROVA                SMALLINT REFERENCES TESTES_ENEM(CODIGO_PROVA),
    POSICAO                     SMALLINT NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS TESTES_MISQUE(
    -- FK DA TABELA DE CONTAS (ESTABELECE UMA RELAÇÃO DE UM PRA MUITOS, UMA CONTA PARA VÁRIOS TESTES_MISQUE) --
    NICK_CONTA                   VARCHAR(20) REFERENCES CONTAS(NICK),

    ID_TESTE                     SERIAL PRIMARY KEY,
    CRIADO                       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INICIADO                     TIMESTAMP,
    TERMINADO                    TIMESTAMP
);

-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS QUESTOES_MISQUE(
    -- FKS DA TABELA DE QUESTOES_ENEM --
    CODIGO_ITEM                  SMALLINT NOT NULL,

    -- FKS DA TABELA DE TESTES_MISQUE --
    ID_TESTE                     INTEGER REFERENCES TESTES_MISQUE(ID_TESTE),
    -- RESPOSTA DO USUÁRIO, PRECISA SER COMPUTADA PARA AVERIGUAR SE ESTÁ CORRETA. --
    RESPOSTA_MISQUE              CHAR,

    -- ASSEGURAR QUE NUNHUMA QUESTÃO SE REPETIRÁ PARA UM TESTE MISQUE  --
    CONSTRAINT IDENTIFICACAO_DA_QUESTAO_ENEM UNIQUE(CODIGO_ITEM, ID_TESTE)
);

-------------------------------------------------------------------------------
------------ FUNÇÕES E VIEWS PARA MAIS FÁCIL MANIPULAÇÃO DOS DADOS ------------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-- GERA A ORDEM EM QUE OS TESTES_MISQUE SÃO CRIADOS DE ACORDO COM O NICK E
-- TIMESTAMP DE CRIAÇÃO PARA USO DA VIEW TESTES_MISQUE_ORDINAL
CREATE FUNCTION GERAR_ORDINAIS_TESTES_MISQUE(
    IN NICK VARCHAR(20),
    IN CR TIMESTAMP,
    OUT ORDINAL INTEGER
) AS $$ WITH ORDINAIS_TST AS(
    SELECT ROW_NUMBER() OVER(
            ORDER BY CRIADO ASC
        ) AS ORDINAL,
        CRIADO
    FROM TESTES_MISQUE
    WHERE NICK_CONTA = NICK
    ORDER BY CRIADO ASC
)
SELECT ORDINAL
FROM ORDINAIS_TST
WHERE CRIADO = CR $$LANGUAGE SQL;

-------------------------------------------------------------------------------
CREATE VIEW TESTES_MISQUE_ORDINAL AS(
    SELECT *,
        GERAR_ORDINAIS_TESTES_MISQUE(NICK_CONTA, CRIADO) AS ORDINAL
    FROM TESTES_MISQUE
);
