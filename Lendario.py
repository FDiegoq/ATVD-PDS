from Pokemon import Pokemon

class pokemon_lendario(Pokemon):
    def __init__(self, nome, tipo, nivel, ataque, defesa, hp):
        self.nome= nome
        self.tipo= tipo
        self.nivel= nivel
        self.ataque= ataque
        self.defesa= defesa
        self.hp= hp

    def showname(self):
        print("Meu nome é:")

    def modoataque(self):
        print("Meu modo de ataque é:")

    def nivel(self):
        print("Meu nivel é:")

    

