from model.curso import Curso
from infra.log import Log
cursos_db = []

class CursoJaExiste(Exception):
    pass


def listar():
    return cursos_db

def cria(id, nome):
    if localizar(id) != None:
            raise CursoJaExiste()
    log = Log(None)
    criado = Curso(id, nome)
    cursos_db.append(criado)
    log.finalizar(criado)
    return cursos_db

def localizar(matricula):
    if cursos_db == []:
            return None
    for curso in cursos_db:
        if curso.id == matricula:
            return curso
    return None

def remover(matricula):
    for x in range(len(cursos_db)):
        if cursos_db[x].id == matricula:
            log = Log(cursos_db[x])
            cursos_db.pop(x)
            remove_curso_disciplina_ofertada(matricula)
            log.finalizar(None)
            return cursos_db
    return None

def remove_curso_disciplina_ofertada(matricula):
    from disciplina_ofertada_api import disciplinas_ofertadas_db

    for disciplina_ofertada in disciplinas_ofertadas_db:
        if disciplina_ofertada.id_curso == matricula:
            disciplina_ofertada.id_curso = None

def atualizar(localizador, matricula, nome):
    for x in range(len(cursos_db)):
        if cursos_db[x].id == localizador:
            duplicado = localizar(matricula)
            if duplicado == None:
                log = Log(cursos_db[x])
                cursos_db[x] = cursos_db[x].atualiza(matricula, nome)
                atualiza_curso_disciplina_ofertada(localizador, matricula)
                log.finalizar(cursos_db[x])
                return cursos_db[x]
            else:
                raise CursoJaExiste()
    return None

def atualiza_curso_disciplina_ofertada(localizador, matricula):
        from disciplina_ofertada_api import disciplinas_ofertadas_db

        for disciplina_ofertada in disciplinas_ofertadas_db:
                if disciplina_ofertada.id_curso == localizador:
                        disciplina_ofertada.id_curso = matricula