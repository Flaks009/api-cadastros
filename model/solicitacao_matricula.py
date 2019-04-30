#id: inteiro, id_aluno: inteiro, id_disciplina_ofertada: inteiro, dt_solicitacao: date, id_coordenador: inteiro, status: inteiro
class Solicitacao_matricula():
    def __init__(self, id, id_aluno, id_disciplina_ofertada, id_coordenador, dt_solicitacao, status):
        self.__id = id
        self.__id_aluno = id_aluno
        self.__id_disciplina_ofertada = id_disciplina_ofertada
        self.__id_coordenador = id_coordenador
        self.__dt_solicitacao = dt_solicitacao
        self.__status = status

    def atualiza(self, id, id_aluno, id_disciplina_ofertada, id_coordenador, dt_solicitacao, status):

        self.__id = id
        self.__id_aluno = id_aluno
        self.__id_disciplina_ofertada = id_disciplina_ofertada
        self.__id_coordenador = id_coordenador
        self.__dt_solicitacao = dt_solicitacao
        self.__status = status

        return self
    

    @property
    def id(self):
        return self.__id

    @property
    def id_aluno(self):
        return self.__id_aluno

    @id_aluno.setter
    def id_aluno(self, id_aluno):
        self.__id_aluno = id_aluno

    @property
    def id_disciplina_ofertada(self):
        return self.__id_disciplina_ofertada
    @id_disciplina_ofertada.setter
    def id_disciplina_ofertada(self, id_disciplina_ofertada):
        self.__id_disciplina_ofertada = id_disciplina_ofertada

    @property
    def id_coordenador(self):
        return self.__id_coordenador
    @id_coordenador.setter
    def id_coordenador(self, id_coordenador):
        self.__id_coordenador = id_coordenador
    
    @property
    def dt_solicitacao(self):
        return self.__dt_solicitacao
    
    @property
    def status(self):
        return self.__status