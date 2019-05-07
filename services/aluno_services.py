from model.aluno import Aluno
from infra.log import Log
from dao.aluno_dao import \
        listar as listar_dao, \
        localizar as localizar_dao, \
        criar as criar_dao, \
        remover as remover_dao, \
        atualizar as atualizar_dao

class AlunoJaExiste(Exception):
        pass

class AlunoNaoExiste(Exception):
        pass


def listar():
    return listar_dao()

def cria(id, nome):
    if localizar(id) != None:
            raise AlunoJaExiste()    
    log = Log(None)    
    criado = Aluno(id, nome)
    criar_dao(criado)
    log.finalizar(criado)
    return listar()

def localizar(matricula):
    return localizar_dao(matricula)

def remover(matricula):
    if localizar(matricula):
        remover_dao(matricula)
        return listar()
    raise AlunoNaoExiste()

def remove_aluno_solicitacao_matricula(matricula):
    from solicitacao_matricula_api import solicitacao_matricula_db

    for solicitacao_matricula in solicitacao_matricula_db:
        if solicitacao_matricula.id_aluno == matricula:
            solicitacao_matricula.id_aluno = None

def atualizar(localizador, matricula, nome):
    if localizar(localizador): 
        atualizar_dao(localizador, matricula, nome)
        return localizar(matricula)
    raise AlunoNaoExiste()


def atualiza_aluno_solicitacao_matricula(localizador, matricula):
        from solicitacao_matricula_api import solicitacao_matricula_db

        for solicitacao_matricula in solicitacao_matricula_db:
                if solicitacao_matricula.id_aluno == localizador:
                        solicitacao_matricula.id_aluno = matricula

