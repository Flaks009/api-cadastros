from model.coordenador import Coordenador
from infra.log import Log
coordenadores_db = []

class CoordenadorJaExiste(Exception):
    pass

def listar():
    return coordenadores_db

def cria(id, nome):
    if localizar(id) != None:
        raise CoordenadorJaExiste()
    log = Log(None)
    criado = Coordenador(id, nome)
    coordenadores_db.append(criado)
    log.finalizar(criado)
    return coordenadores_db

def localizar(matricula):
    if coordenadores_db == []:
        return None
    for coordenador in coordenadores_db:
        if coordenador.id == matricula:
            return coordenador
    return None

def remover(matricula):

    for x in range(len(coordenadores_db)):
        if coordenadores_db[x].id == matricula:
            log = Log(coordenadores_db[x])
            coordenadores_db.pop(x)
            remove_coordenador_disciplina(matricula)
            remove_coordenador_solicitacao(matricula)
            log.finalizar(None)
            return coordenadores_db
    return None

def remove_coordenador_disciplina(id_coordenador):
        from disciplina_api import disciplinas_db
        for disciplina in disciplinas_db:
                if disciplina.id_coordenador == id_coordenador:
                        disciplina.id_coordenador = None

def remove_coordenador_solicitacao(id_coordenador):
        from services.solicitacao_matricula_services import solicitacao_matricula_db
        for solicitacao in solicitacao_matricula_db:
                if solicitacao.id_coordenador == id_coordenador:
                        solicitacao.id_coordenador = None



def atualizar(localizador, matricula, nome):
    for x in range(len(coordenadores_db)):
        if coordenadores_db[x].id == localizador:
            duplicado = localizar(matricula)
            if duplicado == None:
                log = Log(coordenadores_db[x])
                coordenadores_db[x] = coordenadores_db[x].atualiza(matricula, nome)
                atualiza_coordenador_disciplina(localizador, matricula)
                atualiza_coordenador_solicitacao(localizador, matricula)
                log.finalizar(coordenadores_db[x])
                return coordenadores_db[x]
            else:
                raise CoordenadorJaExiste()
    return None

def atualiza_coordenador_disciplina(localizador, matricula):
        from services.disciplina_services import disciplinas_db
        for disciplina in disciplinas_db:
                if disciplina.id_coordenador == localizador:
                        disciplina.id_coordenador = matricula

def atualiza_coordenador_solicitacao(localizador, matricula):
        from services.solicitacao_matricula_services import solicitacao_matricula_db
        for solicitacao in solicitacao_matricula_db:
                if solicitacao.id_coordenador == localizador:
                        solicitacao.id_coordenador = matricula

