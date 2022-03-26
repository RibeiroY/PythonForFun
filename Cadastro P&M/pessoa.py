from metodoPrincipal import Metodo


class Pessoa(Metodo):
    def __init__(self,CPF, nome, chave):
        super().__init__(nome,chave)
        self.CPF = CPF
    def __repr__(self):
        return str(self.__dict__)
    
    def getCPF(self):
        return self.CPF
    def setCPF(self,CPF):
        self.CPF = CPF