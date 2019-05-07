from model.curso import Curso
from infra.log import Log
from dao.curso_dao import \
        listar as listar_dao, \
        localizar as localizar_dao, \
        criar as criar_dao, \
        remover as remover_dao, \
        atualizar as atualizar_dao



cursos_db = []

class CursoJaExiste(Exception):
    pass


def listar():
    return listar_dao()

def cria(id, nome):
    if localizar_dao(id) != None:
            raise CursoJaExiste()
    log = Log(None)
    criado = Curso(id, nome)
    criar_dao(criado)
    log.finalizar(criado)
    return listar()

def localizar(matricula):
    return localizar_dao(matricula)

def remover(matricula):
    if localizar_dao(matricula):
        return remover_dao(matricula)
    return None

def remove_curso_disciplina_ofertada(matricula):
    from disciplina_ofertada_api import disciplinas_ofertadas_db

    for disciplina_ofertada in disciplinas_ofertadas_db:
        if disciplina_ofertada.id_curso == matricula:
            disciplina_ofertada.id_curso = None

def atualizar(localizador, matricula, nome):
    if localizar_dao(localizador):
        return atualizar_dao(localizador, matricula, nome)
    return None

def atualiza_curso_disciplina_ofertada(localizador, matricula):
        from disciplina_ofertada_api import disciplinas_ofertadas_db

        for disciplina_ofertada in disciplinas_ofertadas_db:
                if disciplina_ofertada.id_curso == localizador:
                        disciplina_ofertada.id_curso = matricula