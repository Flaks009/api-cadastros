from infra.db import con
from wrap_connection import transact
from model.disciplina import Disciplina
from infra.log import Log

sql_criar = "INSERT INTO Disciplina (id, nome, status, plano_ensino, carga_horaria, id_coordenador) VALUES (?,?,?,?,?,?)"

sql_localizar = "SELECT id, nome, status, plano_ensino, carga_horaria, id_coordenador FROM Disciplina WHERE id = ?"

sql_listar = "SELECT id, nome, status, plano_ensino, carga_horaria, id_coordenador FROM Disciplina"

sql_remover = "DELETE FROM Disciplina WHERE id = ?"

sql_atualizar = "UPDATE Disciplina SET id = ?, nome = ?, status = ?, plano_ensino = ?, carga_horaria = ?, id_coordenador = ?  WHERE id = ?"

@transact(con)
def criar(disciplina):
    cursor.execute(sql_criar, (disciplina.id, disciplina.nome, disciplina.status, disciplina.plano_ensino, disciplina.carga_horaria, disciplina.id_coordenador))
    connection.commit()

@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = []
    for id, nome, status, plano_ensino, carga_horaria, id_coordenador in cursor.fetchall():
        resultado.append(Disciplina(id, nome, status, plano_ensino, carga_horaria, id_coordenador))
    return resultado

@transact(con)
def localizar(id):
    cursor.execute(sql_localizar, (id,))
    linha = cursor.fetchone()
    if linha == None:
        return None
    return Disciplina(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])

@transact(con)
def remover(id):
    cursor.execute(sql_remover, (id,))
    connection.commit()

@transact(con)
def atualizar(id_antigo, id_novo, nome, status, plano_ensino, carga_horaria, id_coordenador):
    cursor.execute(sql_atualizar, (id_novo, nome, status, plano_ensino, carga_horaria, id_coordenador, id_antigo))
    connection.commit()