from infra.db import con
from wrap_connection import transact
from model.professor import Professor
from infra.log import Log

sql_criar = "INSERT INTO Professor (id, nome) VALUES (?,?)"

sql_localizar = "SELECT id, nome FROM Professor WHERE id = ?"

sql_listar = "SELECT id, nome FROM Professor"

sql_remover = "DELETE FROM Professor WHERE id = ?"

sql_atualizar = "UPDATE Professor SET id = ?, nome = ?  WHERE id = ?"

@transact(con)
def criar(professor):
    cursor.execute(sql_criar, (professor.id, professor.nome))
    connection.commit()

@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = []
    for id, nome in cursor.fetchall():
        resultado.append(Professor(id, nome))
    return resultado

@transact(con)
def localizar(id):
    cursor.execute(sql_localizar, (id,))
    linha = cursor.fetchone()
    if linha == None:
        return None
    return Professor(linha[0], linha[1])

@transact(con)
def remover(id):
    cursor.execute(sql_remover, (id,))
    connection.commit()

@transact(con)
def atualizar(id_antigo, id_novo, nome):
    cursor.execute(sql_atualizar, (id_novo, nome, id_antigo))
    connection.commit()