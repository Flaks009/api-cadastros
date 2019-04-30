from flask import Flask, jsonify, Blueprint, request
from services.professor_services import *
from infra.to_dict import to_dict, to_dict_list
from infra.validacao import validar_campos
professor_app = Blueprint('professor_app', __name__, template_folder='templates')

campos = ['id', 'nome']
tipos = [int, str]

@professor_app.route('/professor')
def professor():
        lista = listar()
        return jsonify(to_dict_list(lista))


@professor_app.route('/professor', methods = ['POST'])
def novo_professor():
        novo = request.get_json()
        id = novo['id']
        nome = novo['nome']

        if  not validar_campos(novo, campos, tipos):
                return '', 422

        try:
                professor = cria(id, nome)
                return jsonify(to_dict_list(professor))

        except ProfessorJaExiste:  
                return '', 409

@professor_app.route('/professor/<int:id_professor>', methods=['GET'])
def localizar_professor(id_professor):
        localizado = localizar(id_professor)
        if (localizado != None):
                return jsonify(to_dict(localizado))
        return '', 404

@professor_app.route('/professor/<int:id_professor>/delete', methods=['DELETE'])
def remove_professor(id_professor):
        removido = remover(id_professor)
        if (removido != None):
                return jsonify(to_dict_list(removido))
        return '', 404

@professor_app.route('/professor/<int:id_professor>/update', methods=['PUT'])
def atualizar_professor(id_professor):
        atualiza = request.get_json()
        
        if  not validar_campos(atualiza, campos, tipos):
                return '', 422

        try:
                atualizado = atualizar(id_professor, atualiza['id'], atualiza['nome'])
                return jsonify(to_dict(atualizado))
        except ProfessorJaExiste:
                return '', 409