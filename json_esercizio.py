# creare una struttura di input che permetta di accedere a due sistemi:
# 1- prendere dei dati in entrata e scrivere (dumps) un file json, salvando in una lista
# 2- prendere tra una lista un input e caricare i file json 

# parte 2:
# avere un sistema di input multiplo (dico già che voglio fare il dump di n elementi)
# così come un sistema di output multiplo (scelgo di stampare più elementi in output)

import json

database = []

def stampa_dati():
    print("\nDATABASE: ")
    for indice, dato in enumerate(database):
        print(indice, dato)


def crea_dato():
    tipo = input("\nScegli il tipo (1: lista, 2: dizionario) ")
    if tipo == "1":
        lista = crea_lista()
        return lista

    elif tipo == "2":  #  DA IMPLEMENTARE
        print("non ancora implementato :O")


def crea_lista():
    lista = []
    lunghezza = input("Quanti elementi ha la lista? ")
    try:
        lunghezza = int(lunghezza)
    except:
        print("Errore: lunghezza non numerica")
    for i in range(lunghezza):
        valore = input("inserisci il valore numero " + str(i+1) + ": ")
        lista.append(valore)
    return lista


def get_dato():
    stampa_dati()
    indice = input("quale elemento vuoi? (inserire indice): ")
    try:
        indice = int(indice)
    except:
        print("Errore: indice inserito non numerico")
    dato = json.loads(database[indice])
    return dato


def menu():
    scelta = input("\nBuongiorno, cosa vuoi fare? \n1. Dump \n2. Load \n3. Exit \n > ")
    while True:
        if scelta == "1":
            quanti = input("Quanti dati vuoi aggiungere? ")
            quanti = int(quanti)
            for _ in range(quanti):
                dato = crea_dato()
                database.append(json.dumps(dato))

        elif scelta == "2":
            output = []
            quanti = input("Quanti dati vuoi caricare? ")
            quanti = int(quanti)
            for _ in range(quanti):
                dato = get_dato()
                output.append(dato)     
            print("Ecco gli elementi richiesti:", output)

        elif scelta == "3":
            print("Arrivederci!\n")
            break    

        else:
            print("Valore non valido\n")

        scelta = input("\nVuoi fare altro? \n1. Dump \n2. Load \n3. Exit \n > ")

menu()
    



