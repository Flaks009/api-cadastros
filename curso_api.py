from flask import Flask, jsonify, request, Blueprint
from services.curso_services import*
from infra.to_dict import to_dict, to_dict_list
from infra.validacao import validar_campos

curso_app = Blueprint('curso_app', __name__, template_folder='templates')

campos = ['id', 'nome']
tipos = [int, str]

@curso_app.route('/curso')
def curso():
        lista = listar()
        return jsonify(to_dict_list(lista))

@curso_app.route('/curso', methods = ["POST"])
def novo_curso():
        novo = request.get_json()
        id = novo['id']
        nome = novo['nome']

        if not validar_campos(novo, campos, tipos):
                return '', 422

        try:
                curso = cria(id, nome)
                return jsonify(to_dict_list(curso))

        except CursoJaExiste:
                return '', 409

@curso_app.route('/curso/<int:id_curso>', methods = ['GET'])
def localizar_curso(id_curso):
        localizado = localizar(id_curso)
        if localizado != None:
                return jsonify(to_dict(localizado))
        return '', 404

@curso_app.route('/curso/<int:id_curso>/delete', methods=['DELETE'])
def remove_curso(id_curso):
        removido = remover(id_curso)
        if removido != None:
                return jsonify(to_dict_list(removido))
        return '', 404


@curso_app.route('/curso/<int:id_curso>/update', methods=['PUT'])
def atualiza_curso(id_curso):
        atualiza = request.get_json()
        id = atualiza['id']
        nome = atualiza['nome']

        if not validar_campos(atualiza, campos, tipos):
                return '', 422
        
        try:
                atualizado = atualizar(id_curso, id, nome)
                return jsonify(to_dict(atualizado))
        
        except CursoJaExiste:
                return '', 409

