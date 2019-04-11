class Venda:
    __idcliente = None
    __idproduto = None    
    __quantidade = None
    __total = None

    def __init__(self, idcliente, idproduto, quantidade, total):
        self.__idcliente = idcliente
        self._idproduto = idproduto        
        self.__quantidade = quantidade
        self.__total = total

    def getId(self):
        return self.__idcliente

    def getProduto(self):
        return self.__idproduto

    def getQuantidade(self):
        return self.__quantidade

    def getTotal(self):
        return self.__total

    
