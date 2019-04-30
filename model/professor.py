class Professor():
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome

    def atualiza(self, id, nome):
        self.__id = id
        self.__nome = nome
        return self

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome