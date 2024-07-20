class Pokemon:
    def __init__(self, nome, vida, tipo, numeroId):
        self.nome=nome
        self.vida=vida
        self.tipo=tipo
        self.numeroId=numeroId

    def getId(self):
        print(self.numeroId)
        return self.numeroId
    
    def setID(self,newId):
        self.numeroId=newId
        print("novo id:", newId)
        return self.numeroId
    
    def showName(self):
        print("meu nome é:", self.nome)

    def showType(self):
        print("Sou do tipo:", self.tipo)