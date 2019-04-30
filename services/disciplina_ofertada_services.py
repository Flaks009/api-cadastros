from services.professor_services import professores_db
from services.curso_services import cursos_db
from services.disciplina_services import disciplinas_db
from model.disciplina_ofertada import Disciplina_ofertada
from infra.log import Log
disciplinas_ofertadas_db = []

class DisciplinaOfertadaJaExiste(Exception):
    pass

class ErroReferencia(Exception):
    pass

def listar():
    return disciplinas_ofertadas_db

def cria(id, nome, id_disciplina, id_professor, id_curso, ano, semestre, turma, data):
    if localizar(id) != None:
        raise DisciplinaOfertadaJaExiste()
    log = Log(None)
    criado = Disciplina_ofertada(id, nome, id_disciplina, id_professor, id_curso, ano, semestre, turma, data)
    valida = valida_nova_disciplina_ofertada(criado)
    if valida:
        for disciplina_ofertada in disciplinas_ofertadas_db:
            if disciplina_ofertada.id_disciplina == criado.id_disciplina and disciplina_ofertada.ano == criado.ano and disciplina_ofertada.semestre == criado.semestre and disciplina_ofertada.id_curso == criado.id_curso:
                raise DisciplinaOfertadaJaExiste()
        log.finalizar(criado)
        disciplinas_ofertadas_db.append(criado)
        return disciplinas_ofertadas_db
    raise ErroReferencia()

def valida_nova_disciplina_ofertada(nova_disciplina_ofertada):
    from services.professor_services import professores_db
    from services.curso_services import cursos_db
    from services.disciplina_services import disciplinas_db
    for disciplina in disciplinas_db:
        if nova_disciplina_ofertada.id_disciplina == disciplina.id:
            print("disciplinas_db OK")
            for professor in professores_db:
                if nova_disciplina_ofertada.id_professor == professor.id:
                    print("professores_db OK")
                    for curso in cursos_db:
                        if nova_disciplina_ofertada.id_curso == curso.id:
                            print("cursos_db OK")
                            return True                                                       
                        else:
                            return False
                else:
                    return False                
        else:
            return False
    
def localizar(matricula):
    if disciplinas_ofertadas_db == []:
            return None
    for disciplina_ofertada in disciplinas_ofertadas_db:
        if disciplina_ofertada.id == matricula:
            return disciplina_ofertada
    return None

def remover(matricula):

    for x in range (len(disciplinas_ofertadas_db)):
        if disciplinas_ofertadas_db[x].id == matricula:
            log = Log(disciplinas_ofertadas_db[x])
            disciplinas_ofertadas_db.pop(x)
            remove_disciplina_ofertada_solicitacao_matricula(matricula)
            log.finalizar(None)
            return disciplinas_ofertadas_db
    return None

def remove_disciplina_ofertada_solicitacao_matricula(matricula):
    from solicitacao_matricula_api import solicitacao_matricula_db

    for solicitacao_matricula in solicitacao_matricula_db:
        if solicitacao_matricula.id_disciplina_ofertada == matricula:
            solicitacao_matricula.id_disciplina_ofertada = None

def atualizar(localizador, nome, matricula, id_disciplina, id_professor, id_curso, ano, semestre, turma, data):
    for x in range(len(disciplinas_ofertadas_db)):
        if disciplinas_ofertadas_db[x].id == localizador:
            duplicado = localizar(matricula)
            if duplicado == None:
                log = Log(disciplinas_ofertadas_db[x])
                disciplinas_ofertadas_db[x] = disciplinas_ofertadas_db[x].atualiza(matricula, nome,id_disciplina, id_professor, id_curso, ano, semestre, turma, data)
                atualiza_disciplina_ofertada_solicitacao_matricula(localizador, matricula)
                log.finalizar(disciplinas_ofertadas_db[x])
                return disciplinas_ofertadas_db
            else:
                raise DisciplinaOfertadaJaExiste()
    return None

def atualiza_disciplina_ofertada_solicitacao_matricula(localizador, matricula):
        from solicitacao_matricula_api import solicitacao_matricula_db

        for solicitacao_matricula in solicitacao_matricula_db:
                if solicitacao_matricula.id_disciplina_ofertada == localizador:
                        solicitacao_matricula.id_disciplina_ofertada = matricula