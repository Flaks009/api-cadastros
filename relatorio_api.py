from flask import Flask, jsonify, Blueprint, request
from aluno_api import alunos_db
from disciplina_api import disciplinas_db
from professor_api import professores_db
from disciplina_ofertada_api import disciplinas_ofertadas_db
from solicitacao_matricula_api import solicitacao_matricula_db
from curso_api import cursos_db

relatorio_app = Blueprint('relatorio_app', __name__, template_folder='template')

@relatorio_app.route('/relatorio', methods = ['GET'])
def relatorio():
    lista_id = ids_matricula()
    
    for aluno in alunos_db:
        for id_aluno in lista_id:
            if id_aluno['aluno'] == aluno['id']:
                id_aluno['aluno'] = aluno['nome']

    for disciplina in disciplinas_db:
        for id_disciplina in lista_id:
            if id_disciplina['disciplina'] == disciplina['id']:
                id_disciplina['disciplina'] = disciplina['nome']
    
    for professor in professores_db:
        for id_professor in lista_id:
            if id_professor['professor'] == professor['id']:
                id_professor['professor'] = professor['nome']

    return jsonify(lista_id)


def ids_aluno():
    lista_aluno_disciplina = []
    for solicitacao in solicitacao_matricula_db:
        id_aluno = solicitacao['id_aluno']
        id_disciplina_ofertada = solicitacao['id_disciplina_ofertada']
        lista_aluno_disciplina.append([id_aluno, id_disciplina_ofertada])
    return lista_aluno_disciplina

def ids_matricula():
    aluno = ids_aluno()

    lista_matricula = []
    for disciplina_ofertada in disciplinas_ofertadas_db:
        for alunos in aluno:
            if disciplina_ofertada['id'] == alunos[1]:
                id_aluno = alunos[0]
                id_disciplina = disciplina_ofertada['id_disciplina']
                id_professor = disciplina_ofertada['id_professor']
                turma = disciplina_ofertada['turma']
                ano = disciplina_ofertada['ano']
                semestre = disciplina_ofertada['semestre']
                lista_matricula.append({'aluno' : id_aluno, 'disciplina' : id_disciplina, 'professor' : id_professor, 'turma':turma, 'ano':ano, 'semestre':semestre})
    return lista_matricula 

