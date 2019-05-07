from flask import Flask, jsonify, request, Blueprint
from services.coordenador_services import *
from infra.to_dict import to_dict, to_dict_list
from infra.validacao import validar_campos
import sqlite3

coordenador_app = Blueprint('coordenador_app', __name__, template_folder='templates')

campos = ['id', 'nome']
tipos = [int, str]

@coordenador_app.route('/coordenador')
def coordenador():
        lista = listar()
        return jsonify(to_dict_list(lista))


@coordenador_app.route('/coordenador', methods = ["POST"])
def novo_coordenador():
        novo = request.get_json()
        id = novo['id']
        nome = novo['nome']

        if not validar_campos(novo, campos, tipos):
                return '', 422

        try:
                coordenador = cria(id, nome)
                return jsonify(to_dict_list(coordenador))

        except CoordenadorJaExiste:
                return '', 409

@coordenador_app.route('/coordenador/<int:id_coordenador>', methods = ['GET'])
def localizar_coordenador(id_coordenador):
        localizado = localizar(id_coordenador)
        if localizado != None:
                return jsonify(to_dict(localizado))
        return '', 404


@coordenador_app.route('/coordenador/<int:id_coordenador>/delete', methods=['DELETE'])
def remove_coordenador(id_coordenador):
        removido = remover(id_coordenador)
        if removido != None:
                return jsonify(to_dict_list(removido))
        return '', 404


@coordenador_app.route('/coordenador/<int:id_coordenador>/update', methods=['PUT'])
def atualiza_coordenador(id_coordenador):
        atualiza = request.get_json()
        id = atualiza['id']
        nome = atualiza['nome']

        if not validar_campos(atualiza, campos, tipos):
                return '', 422
        
        try:
                atualizado = atualizar(id_coordenador, id, nome)
                return jsonify(to_dict(atualizado))
        
        except CoordenadorJaExiste:
                return '', 409
        
        except CoordenadorNaoExiste:
                return '', 404
        
        except sqlite3.IntegrityError:
                return '', 409