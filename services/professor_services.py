from model.professor import Professor
from infra.log import Log
professores_db = []

class ProfessorJaExiste(Exception):
    pass

def listar():
    return professores_db

def cria(id, nome):
    if localizar(id) != None:
            raise ProfessorJaExiste()    
    log = Log(None)    
    criado = Professor(id, nome)
    professores_db.append(criado)
    log.finalizar(criado)
    return professores_db

def localizar(matricula):
    if professores_db == []:
            return None
    for p in professores_db:
        if p.id == matricula:
            return p
    return None


def remover(matricula):
    for x in range (len(professores_db)):
        if professores_db[x].id == matricula:
            log = Log(professores_db[x])
            professores_db.pop(x)
            remove_professor_disciplina_ofertada(matricula)
            log.finalizar(None)
            return professores_db
    return None

def remove_professor_disciplina_ofertada(matricula):
    from disciplina_ofertada_api import disciplinas_ofertadas_db

    for disciplina_ofertada in disciplinas_ofertadas_db:
        if disciplina_ofertada.id_professor == matricula:
            disciplina_ofertada.id_professor = None

def atualizar(localizador, matricula, nome):
    for x in range(len(professores_db)):
        if professores_db[x].id == localizador:
            duplicado = localizar(matricula)
            if duplicado == None:
                log = Log(professores_db[x])
                professores_db[x] = professores_db[x].atualiza(matricula, nome)
                atualiza_professores_db_disciplina_ofertada(localizador, matricula)
                log.finalizar(professores_db[x])
                return professores_db[x]
            else:
                raise ProfessorJaExiste()
    return None

def atualiza_professores_db_disciplina_ofertada(localizador, matricula):
    from disciplina_ofertada_api import disciplinas_ofertadas_db

    for disciplina_ofertada in disciplinas_ofertadas_db:
        if disciplina_ofertada.id == localizador:
            disciplina_ofertada.id_professor = matricula