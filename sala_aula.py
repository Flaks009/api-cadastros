from flask import Flask, request, jsonify, Blueprint
from professor_api import professor_app
from aluno_api import aluno_app
from coordenador_api import coordenador_app
from curso_api import curso_app
from disciplina_api import disciplina_app
from disciplina_ofertada_api import disciplina_ofertada_app
from solicitacao_matricula_api import solicitacao_matricula_app
#from relatorio_api import relatorio_app
from infra.db import cria_db

app = Flask(__name__)

app.register_blueprint(aluno_app)
app.register_blueprint(professor_app)
app.register_blueprint(curso_app)
app.register_blueprint(coordenador_app)
app.register_blueprint(disciplina_app)
app.register_blueprint(disciplina_ofertada_app)
app.register_blueprint(solicitacao_matricula_app)
#app.register_blueprint(relatorio_app)

@app.route('/')
def all():

    from professor_api import listar as professor_listar
    from aluno_api import listar as aluno_listar
    from coordenador_api import listar as coordenador_listar
    from curso_api import listar as curso_listar
    from disciplina_api import listar as disciplina_listar
    from disciplina_ofertada_api import listar as disciplina_ofertada_listar
    from solicitacao_matricula_api import listar as solicitacao_matricula_listar
    from infra.to_dict import to_dict_list



    database = {

    'Alunos' : to_dict_list(aluno_listar()),
    'Professores' : to_dict_list(professor_listar()),
    'Cursos' : to_dict_list(curso_listar()),
    'Coordenadores' : to_dict_list(coordenador_listar()),
    'Disciplina' : to_dict_list(disciplina_listar()),
    'Disciplinas Ofertadas' : to_dict_list(disciplina_ofertada_listar()),
    'Solicitacao Matricula' : to_dict_list(solicitacao_matricula_listar())
    
    }
    return jsonify(database)

cria_db()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
