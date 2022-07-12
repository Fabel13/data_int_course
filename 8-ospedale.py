# creare un sistema di classi   Ospedale -> Dottore -> (specialistica_dottore)
# ogni oggetto deve poter segnare le sue ore di lavoro
# poi dall'ogg ospedale si deve poter pagare le ore di ogni dipendente


class Ospedale:
    def __init__(self):
        self.dipendenti = []
        
    def aggiungi_dipendente(self, dipendente):
        self.dipendenti.append(dipendente)

    def paga_tutti(self):
        for dip in self.dipendenti:
            dip.conto += dip.ore_lavoro * dip.stipendio_ora     # pago le ore
            dip.ore_lavoro = 0                                  # resetto le ore

    
class Dottore(Ospedale):
    def __init__(self, nome):
        self.nome = nome
        self.conto = 0
        self.ore_lavoro = 0

    def lavora(self, numero_ore):
        self.ore_lavoro += numero_ore


class Dottore_base(Dottore):
    def __init__(self, nome):
        Dottore.__init__(self, nome)
        self.stipendio_ora = 20


class Dottore_pro(Dottore):
    def __init__(self, nome):
        Dottore.__init__(self, nome)
        self.stipendio_ora = 50


ospedale = Ospedale()
dotto_1 = Dottore_base("Astolfo")
dotto_2 = Dottore_pro("Brunilde")

ospedale.aggiungi_dipendente(dotto_1)
ospedale.aggiungi_dipendente(dotto_2)

# giornata lavorativa
dotto_1.lavora(numero_ore = 5)
dotto_2.lavora(numero_ore = 3)

# fine giornata
ospedale.paga_tutti()

# stampa conti dottori (soldi guadagnati) 
for dotto in ospedale.dipendenti:
    print(dotto.nome, dotto.conto)
