from infra.db import con
from wrap_connection import transact
from model.solicitacao_matricula import Solicitacao_matricula
from infra.log import Log

sql_criar = "INSERT INTO Solicitacao_matricula (id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status) VALUES (?,?,?,?,?,?)"

sql_localizar = "SELECT id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status FROM Solicitacao_matricula WHERE id = ?"

sql_listar = "SELECT id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status FROM Solicitacao_matricula"

sql_remover = "DELETE FROM Solicitacao_matricula WHERE id = ?"

sql_atualizar = "UPDATE Solicitacao_matricula SET id = ?, id_aluno = ?, id_disciplina_ofertada = ?, dt_solicitacao = ?, id_coordenador = ?, status = ? WHERE id = ?"

@transact(con)
def criar(solicitacao_matricula):
    cursor.execute(sql_criar, (solicitacao_matricula.id, solicitacao_matricula.id_aluno, solicitacao_matricula.id_disciplina_ofertada, solicitacao_matricula.dt_solicitacao, solicitacao_matricula.id_coordenador, solicitacao_matricula.status))
    connection.commit()

@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = []
    for id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status in cursor.fetchall():
        resultado.append(Solicitacao_matricula(id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status))
    return resultado

@transact(con)
def localizar(id):
    cursor.execute(sql_localizar, (id,))
    linha = cursor.fetchone()
    if linha == None:
        return None
    return Solicitacao_matricula(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])

@transact(con)
def remover(id):
    cursor.execute(sql_remover, (id,))
    connection.commit()

@transact(con)
def atualizar(id_antigo, id_novo, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status):
    cursor.execute(sql_atualizar, (id_novo, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status, id_antigo))
    connection.commit()