from model.disciplina import Disciplina
from infra.log import Log
from dao.disciplina_dao import \
        listar as listar_dao, \
        localizar as localizar_dao, \
        criar as criar_dao, \
        remover as remover_dao, \
        atualizar as atualizar_dao


tipo_status = ['inativa', 'ativa']


class DisciplinaJaExiste(Exception):
    pass

class ErroReferencia(Exception):
    pass

class DisciplinaNaoExiste(Exception):
    pass

def listar():
    return listar_dao()

def cria(id, nome, status, plano_ensino, carga_horaria, id_coordenador):
    if localizar(id) != None:
        raise DisciplinaJaExiste()
    log = Log(None)
    criado = Disciplina(id, nome, tipo_status[status], plano_ensino, carga_horaria, id_coordenador)
    valida = valida_nova_disciplina(criado)
    if valida == None:
        raise ErroReferencia()
    criar_dao(valida)
    log.finalizar(valida)
    return listar()

def valida_nova_disciplina(disciplina_data):
    from dao.coordenador_dao  import localizar as localizar_coordenador_dao
    if localizar_coordenador_dao(disciplina_data.id_coordenador):
        return disciplina_data
    return None

def localizar(matricula):
    return localizar_dao(matricula)

def remover(matricula):
    if localizar(matricula):
        remover_dao(matricula)
        return listar()
    raise DisciplinaNaoExiste()

def remove_disciplina_disciplina_ofertada(matricula):
    from services.disciplina_ofertada_services import disciplinas_ofertadas_db

    for disciplina_ofertada in disciplinas_ofertadas_db:
        if disciplina_ofertada.id_disciplina == matricula:
            disciplina_ofertada.id_disciplina = None

def atualizar(localizador, matricula, nome, status, plano_ensino, carga_horaria, id_coordenador):
    if localizar(localizador):
        atualizar_dao(localizador, matricula, nome, status, plano_ensino, carga_horaria, id_coordenador)
        return localizar(matricula)
    raise DisciplinaNaoExiste()

def atualiza_disciplina_disciplina_ofertada(localizador, matricula):
        from services.disciplina_ofertada_services import disciplinas_ofertadas_db

        for disciplina_ofertada in disciplinas_ofertadas_db:
                if disciplina_ofertada.id_disciplina == localizador:
                        disciplina_ofertada.id_disciplina = matricula
