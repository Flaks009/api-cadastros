from model.disciplina import Disciplina
from services.coordenador_services import coordenadores_db
from infra.log import Log
tipo_status = ['inativa', 'ativa']
disciplinas_db = []

class DisciplinaJaExiste(Exception):
        pass

class ErroReferencia(Exception):
    pass


def listar():
    return disciplinas_db

def cria(id, nome, status, plano_ensino, carga_horaria, id_coordenador):
    if localizar(id) != None:
        raise DisciplinaJaExiste()
    log = Log(None)
    criado = Disciplina(id, nome, tipo_status[status], plano_ensino, carga_horaria, id_coordenador)
    valida = valida_nova_disciplina(criado)
    if valida == None:
        raise ErroReferencia()
    disciplinas_db.append(valida)
    log.finalizar(valida)
    return disciplinas_db

def valida_nova_disciplina(disciplina_data):
    from services.coordenador_services import coordenadores_db
    for coordenador in coordenadores_db:
        if disciplina_data.id_coordenador == coordenador.id:
            return disciplina_data
    return None

def localizar(matricula):
    if disciplinas_db == []:
            return None
    for disciplina in disciplinas_db:
        if disciplina.id == matricula:
            return disciplina
    return None

def remover(matricula):

    for x in range (len(disciplinas_db)):
        if disciplinas_db[x].id == matricula:
            log = Log(disciplinas_db[x])
            disciplinas_db.pop(x)
            remove_disciplina_disciplina_ofertada(matricula)
            log.finalizar(None)
            return disciplinas_db
    return None

def remove_disciplina_disciplina_ofertada(matricula):
    from services.disciplina_ofertada_services import disciplinas_ofertadas_db

    for disciplina_ofertada in disciplinas_ofertadas_db:
        if disciplina_ofertada.id_disciplina == matricula:
            disciplina_ofertada.id_disciplina = None

def atualizar(localizador, matricula, nome, status, plano_ensino, carga_horaria, id_coordenador):
    for x in range(len(disciplinas_db)):
        if disciplinas_db[x].id == localizador:
            duplicado = localizar(matricula)
            if duplicado == None:
                log = Log(disciplinas_db[x])
                disciplinas_db[x] = disciplinas_db[x].atualiza(matricula, nome, status, plano_ensino, carga_horaria, id_coordenador)
                atualiza_disciplina_disciplina_ofertada(localizador, matricula)
                log.finalizar(disciplinas_db[x])
                return disciplinas_db
        else:
                raise DisciplinaJaExiste()
    return None

def atualiza_disciplina_disciplina_ofertada(localizador, matricula):
        from services.disciplina_ofertada_services import disciplinas_ofertadas_db

        for disciplina_ofertada in disciplinas_ofertadas_db:
                if disciplina_ofertada.id_disciplina == localizador:
                        disciplina_ofertada.id_disciplina = matricula
