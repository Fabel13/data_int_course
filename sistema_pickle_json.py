# creare un sistema che accetti in entrata dati json o pickle, li converta, te li faccia modificare
# e poi riconvertire nel tipo contrario (json->pickle, pickle->json)

import json
import pickle


class Pacchetto:
    def __init__(self, conversione, dato):
        self.conversione = conversione
        self.dato = dato

    def carica_dato(self):
        return self.conversione.loads(self.dato)
    
    def stampa(self):
        print(self.carica_dato())


def stampa_db(database):
    print("\nDATABASE:")    
    for indice, oggetto in enumerate(database):
        print(indice, "   ",  oggetto.carica_dato())
    print("")


def modifica_dato(dato):
    if type(dato) == str:
        parola = input("che parola vuoi aggiungere? ")
        dato = dato + parola
    elif type(dato) == dict:
        valore = input("che valore dai al terzo elemento? ")
        dato.update({"c":valore})
    return dato


def aggiorno_dato_conversione(oggetto, dato):
    conversione_old = oggetto.conversione
    if conversione_old == json:
        conversione_new = pickle
    else:
        conversione_new = json
    oggetto = Pacchetto(conversione_new, conversione_new.dumps(dato))
    return oggetto


def menu(database):
    stampa_db(database)
    while(True):
        indice = input("Quale elemento vuoi modificare? (inserire indice) ")
        try:
            indice = int(indice)
        except:
            print("Errore: indice non numerico")
        oggetto = database[indice]  # oggetto selezionato
        dato = oggetto.carica_dato()
        dato = modifica_dato(dato)
        # aggiorno databse con il nuovo dato e inverto la conversione
        database[indice] = aggiorno_dato_conversione(oggetto, dato)
        stampa_db(database)

        altro = input("Vuoi fare altro? ([y]/n) ")
        if altro == "n":
            break


ogg1 = Pacchetto(pickle, pickle.dumps({"a":11, "b":24, "c":11}))
ogg2 = Pacchetto(json, json.dumps("Siamo la classe migliore di "))
database = [ogg1, ogg2]

menu(database)