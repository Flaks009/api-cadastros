from flask import Flask, jsonify, request, Blueprint
from services.disciplina_services import *
from infra.to_dict import to_dict, to_dict_list
from infra.validacao import validar_campos
import sqlite3

disciplina_app = Blueprint('disciplina_app', __name__, template_folder='templates')
#{'id': 0, 'nome': '', 'status': 0, 'plano_ensino' : '', 'carga_horaria': 0, 'id_coordenador': 0}
campos = ['id', 'nome', 'status', 'plano_ensino', 'carga_horaria', 'id_coordenador']
tipos = [int, str, int, str, int, int]

@disciplina_app.route('/disciplina')
def disciplina():
        lista = listar()
        return jsonify(to_dict_list(lista))

@disciplina_app.route('/disciplina', methods = ["POST"])
def nova_disciplina():
        novo = request.get_json()
        id = novo['id']
        nome = novo['nome']
        status = novo['status']
        plano_ensino = novo['plano_ensino']
        carga_horaria = novo['carga_horaria']
        id_coordenador = novo['id_coordenador']

        if not validar_campos(novo, campos, tipos):
                return '', 422

        try:
                disciplina = cria(id, nome, status, plano_ensino, carga_horaria, id_coordenador)
                return jsonify(to_dict_list(disciplina))

        except DisciplinaJaExiste:
                return '', 409
        except ErroReferencia:
                return '', 409

@disciplina_app.route('/disciplina/<int:id_disciplina>', methods = ['GET'])
def localizar_disciplinas_db(id_disciplina):
        localizado = localizar(id_disciplina)
        if localizado != None:
                return jsonify(to_dict(localizado))
        return '', 404

@disciplina_app.route('/disciplina/<int:id_disciplina>/delete', methods=['DELETE'])
def remove_disciplinas_db(id_disciplina):
        removido = remover(id_disciplina)
        if removido != None:
                return jsonify(to_dict_list(removido))
        return '', 404

@disciplina_app.route('/disciplina/<int:id_disciplina>/update', methods=['PUT'])
def atualiza_disciplinas_db(id_disciplina):
        atualiza = request.get_json()
        id = atualiza['id']
        nome = atualiza['nome']
        status = atualiza['status']
        plano_ensino = atualiza['plano_ensino']
        carga_horaria = atualiza['carga_horaria']
        id_coordenador = atualiza['id_coordenador']

        if not validar_campos(atualiza, campos, tipos):
                return '', 422

        try:
                atualizado = cria(id, nome, status, plano_ensino, carga_horaria, id_coordenador)
                return jsonify(to_dict_list(atualizado))

        except DisciplinaJaExiste:
                return '', 409

        except DisciplinaNaoExiste:
                return '', 404

        except sqlite3.IntegrityError:
                return '', 409