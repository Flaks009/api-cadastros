from services.aluno_services import alunos_db
from services.coordenador_services import coordenadores_db
from services.disciplina_ofertada_services import disciplinas_ofertadas_db
from model.solicitacao_matricula import Solicitacao_matricula
from infra.log import Log

tipo_status = [0, 'solicitado', 'indeferido', 'matriculado', 'desistente', 'aprovado', 'reprovado']
solicitacao_matricula_db = []

class SolicitacaoJaExiste(Exception):
    pass
class ErroReferencia(Exception):
    pass

def listar():
    return solicitacao_matricula_db




def cria(id, id_aluno,id_disciplina_ofertada, id_coordenador, dt_solicitacao, status):
    if localizar(id) != None:
        raise SolicitacaoJaExiste()
    log = Log(None)
    criado = Solicitacao_matricula(id, id_aluno,id_disciplina_ofertada, id_coordenador, dt_solicitacao, tipo_status[status])
    valida = valida_nova_solicitacao_matricula(criado)
    if valida:
        log.finalizar(criado)
        solicitacao_matricula_db.append(criado)
        return solicitacao_matricula_db
    raise ErroReferencia()


def valida_nova_solicitacao_matricula(solicitacao_matricula_data):
    from services.aluno_services import alunos_db
    from services.disciplina_ofertada_services import disciplinas_ofertadas_db
    for aluno in alunos_db:
        if aluno.id == solicitacao_matricula_data.id_aluno:
            print("alunos_db OK")
            for disciplina_ofertada in disciplinas_ofertadas_db:
                if disciplina_ofertada.id == solicitacao_matricula_data.id_disciplina_ofertada:
                    print("disciplinas_db Ofertada OK")
                    return True
                else:
                    return False
    return False

def localizar(matricula):
    if solicitacao_matricula_db == []:
            return None
    for solicitacao in solicitacao_matricula_db:
        if solicitacao.id == matricula:
            return solicitacao
    return None


def remover(matricula):
    for x in range(len(solicitacao_matricula_db)):
        if solicitacao_matricula_db[x].id == matricula:
            log = Log(solicitacao_matricula_db[x])
            solicitacao_matricula_db.pop(x)
            log.finalizar(None)
            return solicitacao_matricula_db
    return None


def atualiza(localizador, matricula, id_aluno, id_disciplina_ofertada, id_coordenador, dt_solicitacao, status):
    for x in range(len(solicitacao_matricula_db)):
        if solicitacao_matricula_db[x].id == localizador:
            duplicado = localizar(matricula)
            if duplicado == None:
                log = Log(solicitacao_matricula_db[x])
                solicitacao_matricula_db[x] = solicitacao_matricula_db[x].atualiza(matricula, id_disciplina_ofertada, id_coordenador, dt_solicitacao, status)
                log.finalizar(solicitacao_matricula_db[x])
                return solicitacao_matricula_db[x]
            else:
                raise SolicitacaoJaExiste()
    return None