from pydantic import BaseModel, Field
from typing import List, Optional, Union

class Estado(BaseModel):
    """Classe representa dados de um estado."""
    co_uf: int = Field(title="Código da Unidade Federativa.")
    sg_uf: str = Field(title="Sigal da Unidade Federativa.")

class Municipio(BaseModel):
    """ Classe que representa um municipio. """
    co_municipio:int = Field(title="Código do municipio.")
    co_uf_estado:int = Field(title="Código da Unidade Federativa do estado correspondente.")
    no_municipio:str = Field(title="Nome do município.")

class Participante(BaseModel):
    """ Classe que representa um participante. """
    nu_inscricao: int = Field(title="Número de inscrição do participante.")
    nu_ano: int = Field(title="Ano de realização da prova.")
    nu_idade: int = Field(title="Idade do participante.")
    tp_sexo: bool = Field(title="Sexo do participante.")
    tp_estado_civil: int = Field(title="Estado civil do participante.")
    tp_cor_raca: int = Field(title="Cor/Raça/Etnia do participante.")
    tp_nacionalidade: int = Field(title="Nacionalidade.")
    tp_st_conclusao : str = Field(title="Situação de conclusão do Ensino Médio.")
    tp_ano_concluiu : int = Field(title="Ano de Conclusão do Ensino Médio.")
    tp_ensino: int = Field(title="Tipo de instituição que concluiu ou concluirá o Ensino Médio.")
    in_treineiro: bool = Field(title="Indica se o inscrito fez a prova com intuito de apenas treinar seus conhecimentos.")

class Escola(BaseModel):
    """ Classe que representa uma escola. """
    co_escola: int = Field(title="Código da Escola.")
    tp_dependencia_adm_esc : int = Field(title="Dependência administrativa.")
    tp_localizacao_esc : int = Field(title="Localização.")
    tp_sit_func_esc : int = Field(title="Situação de funcionamento.")

class AtendimentoEspecializado(BaseModel):
    """ Classe que representa um atendimento especializado. """
    in_baixa_visao :bool = Field(title="Indicador de baixa visão.")
    in_cegueira :bool = Field(title="Indicador de cegueira.")
    in_surdez :bool = Field(title="Indicador de surdez.")
    in_deficiencia_auditiva :bool = Field(title="Indicador de deficiência auditiva.")
    in_surdo_cegueira :bool = Field(title="Indicador de surdo-cegueira.")
    in_deficiencia_fisica :bool = Field(title="Indicador de deficiência física.")
    in_deficiencia_mental :bool = Field(title="Indicador de deficiência mental.")
    in_deficit_atencao :bool = Field(title="Indicador de déficit de atenção.")
    in_dislexia :bool = Field(title="Indicador de dislexia.")
    in_discalculia :bool = Field(title="Indicador de discalculia.")
    in_autismo :bool = Field(title="Indicador de autismo.")
    in_visao_monocular :bool = Field(title="Indicador de visão monocular.")
    in_outra_def :bool = Field(title="Indicador de outra deficiência ou condição especial.")

class AtendimentoEspecifico(BaseModel):
    """ Classe que representa um atendimento específico. """
    in_gestante: bool = Field(title="Indicador de gestante.")
    in_lactante: bool = Field(title="Indicador de lactante.")
    in_idoso: bool = Field(title="Indicador de inscrito idoso.")
    in_estuda_classe_hospitalar: bool = Field(title="Indicador de inscrição em Unidade Hospitalar.")

class AtendimentoEeE(BaseModel):
    """ Classe que representa um atendimento específico e especializado. """
    in_sem_recurso: bool = Field(title="Indicador de inscrito que não requisitou nenhum recurso.")
    in_braille: bool = Field(title="Indicador de solicitação de prova em braille.")
    in_ampliada_24: bool = Field(title="Indicador de solicitação de prova superampliada com fonte tamanho 24.")
    in_ampliada_18: bool = Field(title="Indicador de solicitação de prova ampliada com fonte tamanho 18.")
    in_ledor: bool = Field(title="Indicador de solicitação de auxílio para leitura (ledor).")
    in_acesso: bool = Field(title="Indicador de solicitação de sala de fácil acesso.")
    in_transcricao: bool = Field(title="Indicador de solicitação de auxílio para transcrição.")
    in_libras: bool = Field(title="Indicador de solicitação de Tradutor- Intérprete Libras.")
    in_tempo_adicional: bool = Field(title="Indicador de solicitação de tempo adicional.")
    in_leitura_labial: bool = Field(title="Indicador de solicitação de leitura labial.")
    in_mesa_cadeira_rodas: bool = Field(title="Indicador de solicitação de mesa para cadeira de rodas.")
    in_mesa_cadeira_separada: bool = Field(title="Indicador de solicitação de mesa e cadeira separada.")
    in_apoio_perna: bool = Field(title="Indicador de solicitação de apoio de perna e pé.")
    in_guia_interprete: bool = Field(title="Indicador de solicitação de guia intérprete.")
    in_computador: bool = Field(title="Indicador de solicitação de computador.")
    in_cadeira_especial: bool = Field(title="Indicador de solicitação de cadeira especial.")
    in_cadeira_canhoto: bool = Field(title="Indicador de solicitação de cadeira para canhoto.")
    in_cadeira_acolchoada: bool = Field(title="Indicador de solicitação de cadeira acolchoada.")
    in_prova_deitado: bool = Field(title="Indicador de solicitação para fazer prova deitado em maca ou mobiliário similar.")
    in_mobiliario_obeso: bool = Field(title="Indicador de solicitação de mobiliário adequado para obeso.")
    in_lamina_overlay: bool = Field(title="Indicador de solicitação de lâmina overlay.")
    in_protetor_auricular: bool = Field(title="Indicador de solicitação de protetor auricular.")
    in_medidor_glicose: bool = Field(title="Indicador de solicitação de medidor de glicose e/ou aplicação de insulina.")
    in_maquina_braile: bool = Field(title="Indicador de solicitação de máquina Braile e/ou Reglete e Punção.")
    in_soroban: bool = Field(title="Indicador de solicitação de soroban.")
    in_marca_passo: bool = Field(title="Indicador de solicitação de marca-passo (impeditivo de uso de detector de metais).")
    in_sonda: bool = Field(title="Indicador de solicitação de sonda com troca periódica.")
    in_medicamentos: bool = Field(title="Indicador de solicitação de medicamentos.")
    in_sala_individual: bool = Field(title="Indicador de solicitação de sala especial individual.")
    in_sala_especial: bool = Field(title="Indicador de solicitação de sala especial até 20 participantes.")
    in_sala_acompanhante: bool = Field(title="Indicador de solicitação de sala reservada para acompanhantes.")
    in_mobiliario_especifico: bool = Field(title="Indicador de solicitação de mobiliário específico.")
    in_material_especifico: bool = Field(title="Indicador de solicitação de material específico.")
    in_nome_social: bool = Field(
        title="Indicador de inscrito que se declarou travesti,"
        " transexual ou transgênero e solicitou atendimento pel"
        "o Nome Social, conforme é reconhecido socialmente em c"
        "onsonância com sua identidade de gênero."
    )

class DadosProvaObjetiva(BaseModel):
    """ Classe que representa os dados da prova objetiva de alguem em um dado ano. """
    presenca_cn: int = Field(title="Presença na prova objetiva de Ciências da Natureza.")
    presenca_ch: int = Field(title="Presença na prova objetiva de Ciências Humanas.")
    presenca_lc: int = Field(title="Presença na prova objetiva de Linguagens e Códigos.")
    presenca_mt: int = Field(title="Presença na prova objetiva de Matemática.")
    prova_cn: int = Field(title="Código do tipo de prova de Ciências da Natureza.")
    prova_ch: int = Field(title="Código do tipo de prova de Ciências Humanas.")
    prova_lc: int = Field(title="Código do tipo de prova de Linguagens e Códigos.")
    prova_mt: int = Field(title="Código do tipo de prova de Matemática.")
    nu_nota_cn: int = Field(title="Nota da prova de Ciências da Natureza.")
    nu_nota_ch: int = Field(title="Nota da prova de Ciências Humanas.")
    nu_nota_lc: int = Field(title="Nota da prova de Linguagens e Códigos")
    nu_nota_mt: int = Field(title="Nota da prova de Matemática")
    tp_lingua : bool = Field(title="Língua Estrangeira.")

class DadosRedacao(BaseModel):
    """ Classe que representa os dados da prova de redação """
    tp_status_redacao: int = Field(title="Situação da redação do participante.")
    nu_nota_comp1:int = Field(title="Nota da competência 1 - Demonstrar domínio da modalidade escrita formal da Língua Portuguesa.")
    nu_nota_comp2:int = Field(title="Nota da competência 2 - Compreender a proposta de redação e aplicar conceitos das várias áreas de conhecimento para desenvolver o tema, dentro dos limites estruturais do texto dissertativo-argumentativo em prosa.")
    nu_nota_comp3:int = Field(title="Nota da competência 3 - Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos em defesa de um ponto de vista.")
    nu_nota_comp4:int = Field(title="Nota da competência 4 - Demonstrar conhecimento dos mecanismos linguísticos necessários para a construção da argumentação.")
    nu_nota_comp5:int = Field(title="Nota da competência 5 - Elaborar proposta de intervenção para o problema abordado, respeitando os direitos humanos.")
    nu_nota_redacao:int = Field(title="Nota da prova de redação.")

class RespostasQuestionario(BaseModel):
    """ Classe que representa as respostas do questionário. """
    Q001 :str = Field(title="Até que série seu pai, ou o homem responsável por você, estudou?")
    Q002 :str = Field(title="Até que série sua mãe, ou a mulher responsável por você, estudou?")
    Q003 :str = Field(title="A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você. (Se ele não estiver trabalhando, escolha uma ocupação pensando no último trabalho dele).")
    Q004 :str = Field(title="A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você. (Se ela não estiver trabalhando, escolha uma ocupação pensando no último trabalho dela).")
    Q005 :str = Field(title="Incluindo você, quantas pessoas moram atualmente em sua residência?")
    Q006 :str = Field(title="Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)")
    Q007 :str = Field(title="Em sua residência trabalha empregado(a) doméstico(a)?")
    Q008 :str = Field(title="Na sua residência tem banheiro?")
    Q009 :str = Field(title="Na sua residência tem quartos para dormir?")
    Q010 :str = Field(title="Na sua residência tem carro?")
    Q011 :str = Field(title="Na sua residência tem motocicleta?")
    Q012 :str = Field(title="Na sua residência tem geladeira?")
    Q013 :str = Field(title="Na sua residência tem freezer (independente ou segunda porta da geladeira)?")
    Q014 :str = Field(title="Na sua residência tem máquina de lavar roupa? (o tanquinho NÃO deve ser considerado)")
    Q015 :str = Field(title="Na sua residência tem máquina de secar roupa (independente ou em conjunto com a máquina de lavar roupa)?")
    Q016 :str = Field(title="Na sua residência tem forno micro-ondas?")
    Q017 :str = Field(title="Na sua residência tem máquina de lavar louça?")
    Q018 :str = Field(title="Na sua residência tem aspirador de pó?")
    Q019 :str = Field(title="Na sua residência tem televisão em cores?")
    Q020 :str = Field(title="Na sua residência tem aparelho de DVD?")
    Q021 :str = Field(title="Na sua residência tem TV por assinatura?")
    Q022 :str = Field(title="Na sua residência tem telefone celular?")
    Q023 :str = Field(title="Na sua residência tem telefone fixo?")
    Q024 :str = Field(title="Na sua residência tem computador?")
    Q025 :str = Field(title="Na sua residência tem acesso à Internet?")
