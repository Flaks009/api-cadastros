from model.professor import Professor
from infra.log import Log
from dao.professor_dao import \
        listar as listar_dao, \
        localizar as localizar_dao, \
        criar as criar_dao, \
        remover as remover_dao, \
        atualizar as atualizar_dao


class ProfessorJaExiste(Exception):
    pass

class ProfessorNaoExiste(Exception):
    pass

def listar():
    return listar_dao()

def cria(id, nome):
    if localizar(id) != None:
            raise ProfessorJaExiste()    
    log = Log(None)    
    criado = Professor(id, nome)
    criar_dao(criado)
    log.finalizar(criado)
    return listar()

def localizar(matricula):
    return localizar_dao(matricula)


def remover(matricula):
    if localizar_dao(matricula):
        remover_dao(matricula)
        return listar()
    raise ProfessorNaoExiste()

def remove_professor_disciplina_ofertada(matricula):
    from disciplina_ofertada_api import disciplinas_ofertadas_db

    for disciplina_ofertada in disciplinas_ofertadas_db:
        if disciplina_ofertada.id_professor == matricula:
            disciplina_ofertada.id_professor = None

def atualizar(localizador, matricula, nome):
    if localizar(localizador):
        atualizar_dao(localizador, matricula, nome)
        return localizar(matricula)
    raise ProfessorNaoExiste()

def atualiza_professores_db_disciplina_ofertada(localizador, matricula):
    from disciplina_ofertada_api import disciplinas_ofertadas_db

    for disciplina_ofertada in disciplinas_ofertadas_db:
        if disciplina_ofertada.id == localizador:
            disciplina_ofertada.id_professor = matricula