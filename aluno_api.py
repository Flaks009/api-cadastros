from flask import Flask, jsonify, request, Blueprint
from services.aluno_services import *
from infra.to_dict import to_dict, to_dict_list
from infra.validacao import validar_campos
import sqlite3

aluno_app = Blueprint('aluno_app', __name__, template_folder='templates')

campos = ['id', 'nome']
tipos = [int, str]


@aluno_app.route('/aluno')
def aluno():
        lista = listar()
        return jsonify(to_dict(lista))

@aluno_app.route('/aluno', methods = ["POST"])
def novo_aluno():
        novo = request.get_json()
        id = novo['id']
        nome = novo['nome']

        if  not validar_campos(novo, campos, tipos):
                return '', 422

        try:
                aluno = cria(id, nome)
                return jsonify(to_dict_list(aluno))

        except AlunoJaExiste:  
                return '', 409
        


@aluno_app.route('/aluno/<int:id_aluno>', methods=['GET'])
def localizar_aluno(id_aluno):
        localizado = localizar(id_aluno)
        if localizado != None:
                return jsonify(to_dict(localizado))
        return '', 404
                


@aluno_app.route('/aluno/<int:id_aluno>/delete', methods=['DELETE'])
def remove_aluno(id_aluno):
        removido = remover(id_aluno)
        if removido != None:
                return jsonify(to_dict_list(removido))
        return '', 404



@aluno_app.route('/aluno/<int:id_aluno>/update', methods=['PUT'])
def atualiza_aluno(id_aluno):
        atualiza = request.get_json()
        
        if  not validar_campos(atualiza, campos, tipos):
                return '', 422

        try:
                atualizado = atualizar(id_aluno, atualiza['id'], atualiza['nome'])
                return jsonify(to_dict(atualizado))
        except AlunoJaExiste:
                return '', 409

        except sqlite3.IntegrityError:
                return '', 409

        except AlunoNaoExiste:
                return '', 404
