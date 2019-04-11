class Produto:
    __idproduto = None
    __nome = None    
    __valor = None
    

    def __init__(self, idproduto, nome, valor):
        self.__idproduto = idproduto
        self.__nome = nome        
        self.__valor = valor
     
    def getId(self):
        return self.__idproduto

    def getNome(self):
        return self.__nome

    def getValor(self):
        return self.__valor

    
