from model.disciplina_ofertada import Disciplina_ofertada
from infra.log import Log
from dao.disciplina_ofertada_dao import \
        listar as listar_dao, \
        localizar as localizar_dao, \
        criar as criar_dao, \
        remover as remover_dao, \
        atualizar as atualizar_dao



disciplinas_ofertadas_db = []

class DisciplinaOfertadaJaExiste(Exception):
    pass

class ErroReferencia(Exception):
    pass

class DisciplinaOfertadaNaoExiste(Exception):
    pass


def listar():
    return listar_dao()

def cria(id, id_disciplina, id_professor, id_curso, ano, semestre, turma, data):
    if localizar(id) != None:
        raise DisciplinaOfertadaJaExiste()
    log = Log(None)
    criado = Disciplina_ofertada(id, id_disciplina, id_professor, id_curso, ano, semestre, turma, data)
    valida = valida_nova_disciplina_ofertada(criado)
    if valida:
        for disciplina_ofertada in listar():
            if disciplina_ofertada[2] == criado.id_disciplina and disciplina_ofertada[5] == criado.ano and disciplina_ofertada[6] == criado.semestre and disciplina_ofertada[4] == criado.id_curso:
                raise DisciplinaOfertadaJaExiste()
        log.finalizar(criado)
        criar_dao(criado)
        return listar()
    raise ErroReferencia()

def valida_nova_disciplina_ofertada(nova_disciplina_ofertada):
    from dao.professor_dao import localizar as localizar_dao_professor
    from dao.curso_dao import localizar as localizar_dao_curso
    from dao.disciplina_dao import localizar as localizar_dao_disciplina

    if localizar_dao_professor(nova_disciplina_ofertada.id_professor):
        if localizar_dao_curso(nova_disciplina_ofertada.id_curso):
            if localizar_dao_disciplina(nova_disciplina_ofertada.id_disciplina):
                return True
            return False
        return False
    return False
    
def localizar(matricula):
    return localizar_dao(matricula)

def remover(matricula):
    if localizar_dao(matricula):
        remover_dao(matricula)
        return listar()
    raise DisciplinaOfertadaNaoExiste()

def remove_disciplina_ofertada_solicitacao_matricula(matricula):
    from solicitacao_matricula_api import solicitacao_matricula_db

    for solicitacao_matricula in solicitacao_matricula_db:
        if solicitacao_matricula.id_disciplina_ofertada == matricula:
            solicitacao_matricula.id_disciplina_ofertada = None

def atualizar(localizador, matricula, id_disciplina, id_professor, id_curso, ano, semestre, turma, data):
    if localizar_dao(localizador):
        atualizar_dao(localizador, matricula, id_disciplina, id_professor, id_curso, ano, semestre, turma, data)
        return localizar(matricula)
    raise DisciplinaOfertadaNaoExiste()

def atualiza_disciplina_ofertada_solicitacao_matricula(localizador, matricula):
        from solicitacao_matricula_api import solicitacao_matricula_db

        for solicitacao_matricula in solicitacao_matricula_db:
                if solicitacao_matricula.id_disciplina_ofertada == localizador:
                        solicitacao_matricula.id_disciplina_ofertada = matricula