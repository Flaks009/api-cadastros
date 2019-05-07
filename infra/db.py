import sqlite3
from wrap_connection import transact

create_sqls = ["""
CREATE TABLE IF NOT EXISTS Aluno
(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL

);""", """

CREATE TABLE IF NOT EXISTS Professor
(

    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL


);""", """

CREATE TABLE IF NOT EXISTS Coordenador
(

    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL


);""", """

CREATE TABLE IF NOT EXISTS Curso
(

    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL


);""", """

CREATE TABLE IF NOT EXISTS Disciplina
(

    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    status TEXT NOT NULL,
    plano_ensino TEXT NOT NULL,
    carga_horaria INTEGER NOT NULL,
    id_coordenador INTEGER,
    FOREIGN KEY(id_coordenador) REFERENCES Coordenador(id) ON UPDATE CASCADE ON DELETE SET NULL
);""", """

CREATE TABLE IF NOT EXISTS Disciplina_ofertada
(

    id INTEGER PRIMARY KEY,
    ano INTEGER NOT NULL,
    semestre INTEGER NOT NULL,
    turma INTEGER NOT NULL,
    data DATE NOT NULL,
    id_professor INTEGER,
    id_disciplina INTEGER,
    id_curso INTEGER,
    FOREIGN KEY(id_disciplina) REFERENCES Disciplina(id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY(id_professor) REFERENCES Professor(id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY(id_curso) REFERENCES Curso(id) ON UPDATE CASCADE ON DELETE SET NULL

);""", """

CREATE TABLE IF NOT EXISTS Solicitacao_matricula
(

    id INTEGER PRIMARY KEY,
    dt_solicitacao date NOT NULL,
    status INTEGER NOT NULL,
    id_aluno INTEGER,
    id_disciplina_ofertada INTEGER,
    id_coordenador INTEGER,
    FOREIGN KEY(id_aluno) REFERENCES Aluno(id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY(id_disciplina_ofertada) REFERENCES Disciplina_ofertada(id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY(id_coordenador) REFERENCES Coordenador(id) ON UPDATE CASCADE ON DELETE SET NULL

);
"""]


def con():
    return sqlite3.connect("lms.db")


@transact(con)
def cria_db():
    for sql in create_sqls:
        cursor.execute(sql)
    connection.commit()
