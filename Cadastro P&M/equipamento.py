from metodoPrincipal import Metodo

class Equipamento(Metodo):
    def __init__(self,setor, nome, chave):
        super().__init__(nome,chave)
        self.setor = setor 
    def __repr__(self):
        return str(self.__dict__)

    def getSetor(self):
        return self.setor
    def setSetor(self,setor):
        self.setor = setor