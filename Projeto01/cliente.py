class Cliente:
    __idcliente = None
    __nome = None    
    __idade = None
    __cidade = None

    def __init__(self, idcliente, nome, idade, cidade):
        self.__idcliente = idcliente
        self.__nome = nome        
        self.__idade = idade
        self.__cidade = cidade

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getCidade(self):
        return self.__cidade

    def getName(self, idcliente):
        retorno = ""
        if(self.__idcliente == idcliente):
            retorno = self.__nome
        else:
            retorno = "Cliente nao encontrado!!"
        return (retorno)
