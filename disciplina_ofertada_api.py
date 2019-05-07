from flask import Flask, jsonify, request, Blueprint
from services.disciplina_ofertada_services import *
from infra.to_dict import to_dict, to_dict_list
from infra.validacao import validar_campos
import sqlite3

disciplina_ofertada_app = Blueprint('disciplina_ofertada_app', __name__, template_folder='templates')
#id: inteiro, nome: texto, id_disciplina: inteiro, id_professor: inteiro, ano: inteiro, semestre: inteiro, turma: texto, id_curso: inteiro, data: date
campos = ['id', 'id_disciplina', 'id_professor', 'id_curso', 'ano', 'semestre', 'turma', 'data']
tipos = [int, int, int, int, int, int, str, str]

@disciplina_ofertada_app.route('/disciplina_ofertada')
def disciplina_ofertada():
        lista = listar()
        return jsonify(to_dict_list(lista))

@disciplina_ofertada_app.route('/disciplina_ofertada', methods = ["POST"])
def nova_disciplina_ofertada():
        print('entrou')
        novo = request.get_json()
        id = novo['id']
        id_disciplina = novo['id_disciplina']
        id_professor = novo['id_professor']
        id_curso = novo['id_curso']
        ano = novo['ano']
        semestre = novo['semestre']
        turma = novo['turma']
        data = novo['data']

        if  not validar_campos(novo, campos, tipos):
                return '', 422

        try:
                disciplina_ofertada = cria(id, id_disciplina, id_professor, id_curso, ano, semestre, turma, data)
                return jsonify(to_dict_list(disciplina_ofertada))

        except DisciplinaOfertadaJaExiste:  
                return '', 409

        except ErroReferencia:
                return '', 409


@disciplina_ofertada_app.route('/disciplina_ofertada/<int:id_disciplina_ofertada>', methods = ['GET'])
def localizar_disciplina_ofertada(id_disciplina_ofertada):
        localizado = localizar(id_disciplina_ofertada)
        if localizado!= None:
                return jsonify(to_dict(localizado))
        return '', 404

@disciplina_ofertada_app.route('/disciplina_ofertada/<int:id_disciplina_ofertada>/delete', methods=['DELETE'])
def remove_disciplina_ofertada(id_disciplina_ofertada):
        removido = remover(id_disciplina_ofertada)
        if removido != None:
                return jsonify(to_dict_list(removido))
        return '', 404


@disciplina_ofertada_app.route('/disciplina_ofertada/<int:id_disciplina_ofertada>/update', methods=['PUT'])
def atualiza_disciplina_ofertada(id_disciplina_ofertada):
        atualiza = request.get_json()
        id = atualiza['id']
        id_disciplina = atualiza['id_disciplina']
        id_professor = atualiza['id_professor']
        id_curso = atualiza['id_curso']
        ano = atualiza['ano']
        semestre = atualiza['semestre']
        turma = atualiza['turma']
        data = atualiza['data']

        if  not validar_campos(atualiza, campos, tipos):
                return '', 422

        try:
                atualizado = atualizar(id_disciplina_ofertada, id, id_disciplina, id_professor, id_curso, ano, semestre, turma, data)
                return jsonify(to_dict_list(atualizado))

        except DisciplinaOfertadaJaExiste:  
                return '', 409

        except DisciplinaOfertadaNaoExiste:
                return '', 404
        
        except sqlite3.IntegrityError:
                return '', 409