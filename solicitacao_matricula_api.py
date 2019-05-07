from flask import Flask, jsonify, request, Blueprint
from services.solicitacao_matricula_services import *
from infra.to_dict import to_dict, to_dict_list
from infra.validacao import validar_campos
import sqlite3

solicitacao_matricula_app = Blueprint('solicitacao_matricula_app', __name__, template_folder='templates')

#id: inteiro, id_aluno: inteiro, id_disciplina_ofertada: inteiro, dt_solicitacao: date, id_coordenador: inteiro, status: inteiro
campos = ['id', 'id_aluno', 'id_disciplina_ofertada', 'dt_solicitacao', 'id_coordenador', 'status']
tipos = [int, int, int, str, int, int]

@solicitacao_matricula_app.route('/solicitacao_matricula')
def solicitacao_matricula():
        lista = listar()
        return jsonify(to_dict_list(lista))

@solicitacao_matricula_app.route('/solicitacao_matricula', methods = ["POST"])
def nova_solicitacao_matricula():
        
        novo = request.get_json()
        id = novo['id']
        id_aluno = novo['id_aluno']
        id_disciplina_ofertada = novo['id_disciplina_ofertada']
        dt_solicitacao = novo['dt_solicitacao']
        id_coordenador = novo['id_coordenador']
        status = novo['status']

        if  not validar_campos(novo, campos, tipos):
                return '', 422

        try:
                solicitacao = cria(id, id_aluno,id_disciplina_ofertada, id_coordenador, dt_solicitacao, status)
                return jsonify(to_dict_list(solicitacao))

        except SolicitacaoJaExiste:  
                return '', 409
        
        except ErroReferencia:
                return '', 409

        

@solicitacao_matricula_app.route('/solicitacao_matricula/<int:id_solicitacao_matricula>', methods = ['GET'])
def localizar_solicitacao_matricula(id_solicitacao_matricula):
        localizado = localizar_solicitacao_matricula(id_solicitacao_matricula)
        if localizado != None:
                return jsonify(to_dict(localizado))
        return '', 404


@solicitacao_matricula_app.route('/solicitacao_matricula/<int:id_solicitacao_matricula>/delete', methods=['DELETE'])
def remove_solicitacao_matricula(id_solicitacao_matricula):
        removido = remover(id_solicitacao_matricula)
        if removido != None:
                return jsonify(to_dict_list(removido))
        return '', 404

@solicitacao_matricula_app.route('/solicitacao_matricula/<int:id_solicitacao_matricula>/update', methods=['PUT'])
def atualiza_solicitacao_matricula(id_solicitacao_matricula):
        atualiza = request.get_json()
        id = atualiza['id']
        id_aluno = atualiza['id_aluno']
        id_disciplina_ofertada = atualiza['id_disciplina_ofertada']
        dt_solicitacao = atualiza['dt_solicitacao']
        id_coordenador = atualiza['id_coordenador']
        status = atualiza['status']

        if  not validar_campos(atualiza, campos, tipos):
                return '', 422

        try:
                atualizado = cria(id, id_aluno,id_disciplina_ofertada, id_coordenador, dt_solicitacao, status)
                return jsonify(to_dict_list(atualizado))

        except SolicitacaoJaExiste:  
                return '', 409
        
        except SolicitacaoNaoExiste:
                return '', 404
        
        except sqlite3.IntegrityError:
                return '', 409

