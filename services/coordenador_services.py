from model.coordenador import Coordenador
from infra.log import Log
from dao.coordenador_dao import \
        listar as listar_dao, \
        localizar as localizar_dao, \
        criar as criar_dao, \
        remover as remover_dao, \
        atualizar as atualizar_dao


class CoordenadorJaExiste(Exception):
    pass

class CoordenadorNaoExiste(Exception):
    pass

def listar():
    return listar_dao()

def cria(id, nome):
    if localizar(id) != None:
        raise CoordenadorJaExiste()
    log = Log(None)
    criado = Coordenador(id, nome)
    criar_dao(criado)
    log.finalizar(criado)
    return listar()

def localizar(matricula):
    return localizar_dao(matricula)

def remover(matricula):
    if localizar(matricula):
        remover_dao(matricula)
        return listar()
    raise CoordenadorNaoExiste()

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
    if localizar(localizador):
        atualizar_dao(localizador, matricula, nome)
        return localizar(matricula)
    return CoordenadorNaoExiste

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

