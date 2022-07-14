# creare un sistema di classi come sotto:
#            Animale
#       /       |       \
#   Felino    Canide   Uccello
#
# le classi figlie vengono create dal padre dopo inserimento tramite input degli attributi e la scelta del tipo di ogg da creare

class Animale:
    def __init__(self, nome):
        self.nome = nome

    def crea_felino(self):
        tipo = "Felino"
        destrezza = input("Quanto è la destrezza del felino? ")
        return Felino(self.nome, tipo, destrezza)

    def crea_canide(self):
        tipo = "Canide"
        forza = input("Quanto è la forza del canide? ")
        return Canide(self.nome, tipo, forza)

    def crea_uccello(self):
        tipo = "Uccello"
        carisma = input("Quanto è il carisma dell'uccello? ")
        return Uccello(self.nome, tipo, carisma)

    def stampa(self):
        print(self.nome)


class Felino(Animale):
    def __init__(self, nome, tipo, destrezza):
        Animale.__init__(self, nome)
        self.tipo = tipo
        self.destrezza = destrezza

    def stampa(self):
        print(self.nome, self.tipo, self.destrezza)


class Canide(Animale):
    def __init__(self, nome, tipo, forza):
        Animale.__init__(self, nome)
        self.tipo = tipo
        self.forza = forza

    def stampa(self):
        print(self.nome, self.tipo, self.forza)


class Uccello(Animale):
    def __init__(self, nome, tipo, carisma):
        Animale.__init__(self, nome)
        self.tipo = tipo
        self.carisma = carisma

    def stampa(self):
        print(self.nome, self.tipo, self.carisma)


start = input("Vuoi un nuovo animale? (y/n) ")

while start == "y":
    nome = input("Come si chiama? ")
    a = Animale(nome)
    scelta = input("Quale animale vuoi?  (felino, canide, uccello)")
    if scelta == "felino":
        a = a.crea_felino()
    elif scelta == "canide":
        a = a.crea_canide()
    elif scelta == "uccello":
        a = a.crea_uccello()
    else:
        print("animale non valido")
        continue
    
    a.stampa()
    start = input("Vuoi un nuovo animale? (y/n) ")

