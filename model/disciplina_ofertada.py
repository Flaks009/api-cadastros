#id: inteiro, nome: texto, id_disciplina: inteiro, id_professor: inteiro, ano: inteiro, semestre: inteiro, turma: texto, id_curso: inteiro, data: date
class Disciplina_ofertada():
    def __init__(self, id, nome, id_disciplina, id_professor, id_curso, ano, semestre, turma, data):
        self.__id = id
        self.__nome = nome
        self.__id_disciplina = id_disciplina
        self.__id_professor = id_professor
        self.__id_curso = id_curso
        self.__ano = ano
        self.__semestre = semestre
        self.__turma = turma
        self.__data = data

    def atualiza(self, id, nome, id_disciplina, id_professor, id_curso, ano, semestre, turma, data):
        self.__id = id
        self.__nome = nome
        self.__id_disciplina = id_disciplina
        self.__id_professor = id_professor
        self.__id_curso = id_curso
        self.__ano = ano
        self.__semestre = semestre
        self.__turma = turma
        self.__data = data
        return self
    
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome
    
    @property
    def id_disciplina(self):
        return self.__id_disciplina
    @id_disciplina.setter
    def id_disciplina(self, id_disciplina):
        self.__id_disciplina = id_disciplina
    
    @property 
    def id_professor(self):
        return self.__id_professor
    
    @id_professor.setter
    def id_professor(self, id_professor):
        self.__id_professor = id_professor
    
    @property
    def id_curso(self):
        return self.__id_curso
    @id_curso.setter
    def id_curso(self, id_curso):
        self.__id_curso = id_curso
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def semestre(self):
        return self.__semestre
    
    @property
    def turma(self):
        return self.__turma
    
    @property
    def data(self):
        return self.__data
    