class Pokemon:
    def __init__(self, nome, vida, tipo,id):
        self.nome=nome
        self.nome=vida
        self.nome=tipo
        self.nome=id

    def getId(self):
        return self.id
    
    def setID(self):
        newId=input('Digite o novo ID:' )
        return self.id
    
    def showName(self):
        print("meu nome é:" )