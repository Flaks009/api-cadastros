from model.aluno import Aluno
from infra.log import Log
alunos_db = []

class AlunoJaExiste(Exception):
        pass

def listar():
    return alunos_db

def cria(id, nome):
    if localizar(id) != None:
            raise AlunoJaExiste()    
    log = Log(None)    
    criado = Aluno(id, nome)
    alunos_db.append(criado)
    log.finalizar(criado)
    return alunos_db

def localizar(matricula):
    if alunos_db == []:
            return None
    for aluno in alunos_db:
        if aluno.id == matricula:
            return aluno
    return None

def remover(matricula):
   
    for x in range(len(alunos_db)):
        if alunos_db[x].id == matricula:
            log = Log(alunos_db[x])    
            alunos_db.pop(x)
            remove_aluno_solicitacao_matricula(matricula)
            log.finalizar(None)
            return alunos_db
    return None

def remove_aluno_solicitacao_matricula(matricula):
    from solicitacao_matricula_api import solicitacao_matricula_db

    for solicitacao_matricula in solicitacao_matricula_db:
        if solicitacao_matricula.id_aluno == matricula:
            solicitacao_matricula.id_aluno = None

def atualizar(localizador,matricula, nome):
    for x in range(len(alunos_db)):
        if alunos_db[x].id == localizador:
            duplicado = localizar(matricula)
            if duplicado == None:
                log = Log(alunos_db[x])      
                alunos_db[x] = alunos_db[x].atualiza(matricula, nome)
                atualiza_aluno_solicitacao_matricula(localizador, matricula)
                log.finalizar(alunos_db[x])
                return alunos_db[x]
            else:
                raise AlunoJaExiste()       
    return None

def atualiza_aluno_solicitacao_matricula(localizador, matricula):
        from solicitacao_matricula_api import solicitacao_matricula_db

        for solicitacao_matricula in solicitacao_matricula_db:
                if solicitacao_matricula.id_aluno == localizador:
                        solicitacao_matricula.id_aluno = matricula

