from services.aluno_services import alunos_db
from services.coordenador_services import coordenadores_db
from services.disciplina_ofertada_services import disciplinas_ofertadas_db
from model.solicitacao_matricula import Solicitacao_matricula
from infra.log import Log
from dao.solicitacao_matricula_dao import \
        listar as listar_dao, \
        localizar as localizar_dao, \
        criar as criar_dao, \
        remover as remover_dao, \
        atualizar as atualizar_dao

tipo_status = [0, 'solicitado', 'indeferido', 'matriculado', 'desistente', 'aprovado', 'reprovado']
solicitacao_matricula_db = []

class SolicitacaoJaExiste(Exception):
    pass
class ErroReferencia(Exception):
    pass

def listar():
    return listar_dao()

def cria(id, id_aluno,id_disciplina_ofertada, id_coordenador, dt_solicitacao, status):
    if localizar(id) != None:
        print("erro")
        raise SolicitacaoJaExiste()
    log = Log(None)
    criado = Solicitacao_matricula(id, id_aluno,id_disciplina_ofertada, id_coordenador, dt_solicitacao, tipo_status[status])
    valida = valida_nova_solicitacao_matricula(criado)
    print(valida)
    if valida:
        log.finalizar(criado)
        criar_dao(criado)
        return listar()
    raise ErroReferencia()


def valida_nova_solicitacao_matricula(solicitacao_matricula_data):
    from dao.aluno_dao import localizar as localizar_dao_aluno
    from dao.disciplina_ofertada_dao import localizar as localizar_dao_disciplinas_ofertadas
    from dao.coordenador_dao import localizar as localizar_dao_coordenador

    if localizar_dao_aluno(solicitacao_matricula_data.id_aluno):
        print("Aluno OK")
        if localizar_dao_disciplinas_ofertadas(solicitacao_matricula_data.id_disciplina_ofertada):
            print("Coordenador OK")
            if localizar_dao_coordenador(solicitacao_matricula_data.id_coordenador):
                print("Disciplina OK")
                return True
            return False
        return False
    return False

def localizar(matricula):
    return localizar_dao(matricula)

def remover(matricula):
    if localizar(matricula):
        return remover_dao(matricula)
    return None

def atualiza(localizador, matricula, id_aluno, id_disciplina_ofertada, id_coordenador, dt_solicitacao, status):
    if localizar(matricula):
        return atualizar_dao(localizador, matricula, id_aluno, id_disciplina_ofertada, id_coordenador, dt_solicitacao, status)
    return None