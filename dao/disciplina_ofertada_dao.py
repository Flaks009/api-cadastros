from infra.db import con
from wrap_connection import transact
from model.disciplina_ofertada import Disciplina_ofertada
from infra.log import Log

sql_criar = "INSERT INTO Disciplina_ofertada (id, id_disciplina, id_professor, id_curso, ano, semestre, turma, data) VALUES (?,?,?,?,?,?,?,?)"

sql_localizar = "SELECT id, id_disciplina, id_professor, id_curso, ano, semestre, turma, data FROM Disciplina_ofertada WHERE id = ?"

sql_listar = "SELECT id, id_disciplina, id_professor, id_curso, ano, semestre, turma, data FROM Disciplina_ofertada"

sql_remover = "DELETE FROM Disciplina_ofertada WHERE id = ?"

sql_atualizar = "UPDATE Disciplina_ofertada SET id = ?, id_disciplina = ?, id_professor = ?, id_curso = ?, ano = ?, semestre = ?, turma = ?, data = ? WHERE id = ?"

@transact(con)
def criar(disciplina_ofertada):
    cursor.execute(sql_criar, (disciplina_ofertada.id, disciplina_ofertada.id_disciplina, disciplina_ofertada.id_professor, disciplina_ofertada.id_curso, disciplina_ofertada.ano, disciplina_ofertada.semestre, disciplina_ofertada.turma, disciplina_ofertada.data))
    connection.commit()

@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = []
    for id, id_disciplina, id_professor, id_curso, ano, semestre, turma, data in cursor.fetchall():
        resultado.append(Disciplina_ofertada(id, id_disciplina, id_professor, id_curso, ano, semestre, turma, data))
    return resultado

@transact(con)
def localizar(id):
    cursor.execute(sql_localizar, (id,))
    linha = cursor.fetchone()
    if linha == None:
        return None
    return Disciplina_ofertada(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7])

@transact(con)
def remover(id):
    cursor.execute(sql_remover, (id,))
    connection.commit()

@transact(con)
def atualizar(id_antigo, id_novo, id_disciplina, id_professor, id_curso, ano, semestre, turma, data):
    cursor.execute(sql_atualizar, (id_novo, id_disciplina, id_professor, id_curso, ano, semestre, turma, data, id_antigo))
    connection.commit()