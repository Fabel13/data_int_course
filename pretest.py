# utilizza una clase ereditata lineare all'interno di una gerarchia non lineare per generare un dict di dati (nome cognome data password) 
# che deve essere conservato nel figlio 1-2 ma modificato nelle classi parallele.
# Le modifiche saranno: cambia parametri, elimina account, crea nuovo account.
# Dovrà essere ripetibile e stampare la lista dei dict presenti

# per ogni dict, poterlo convertitre / deconcertire in json e pickle

# creare una classe archivio che salvi tutte le azioni eseguite all'avvio dello script
# e permetta di stamparle se si conosce la password admin (nuova variabile)


import json, pickle


class Menu:
    def __init__(self):
        pass

    def start(self):
        db = Database()
        modif = Modificatore(db)
        while True:
            testo = "\nSeleziona l'azione desiderata: \n1. Gestione database \n2. Conversione pickle/json \n"
            scelta = input(testo)
            if scelta == "1":                
                modif.start()
            elif scelta == "2":
                modif.converti()


class Database(Menu):
    def __init__(self):
        self.database = []

    def stampa_db(self):
        print("DATABASE:")
        for index, data in enumerate(self.database):
            print(index, " --> ", data)

    def aggiungi(self, account):
        self.database.append(account)

    def rimpiazza(self, indice, account):
        self.database[indice] = account

    def elimina(self, indice):
        self.database.pop(indice)


class Modificatore:
    def __init__(self, db):
        self.db = db
    
    def start(self):
        scelta = input("\nCosa vuoi fare? \n1. Aggiungi un account \n2. Modifica un account \n3. Elimina un account \n4. Stampa database \n")
        while scelta not in ["1", "2", "3", "4"]:
            scelta = input("Scelta non valida, riprova: ")
        if scelta == "1":
            # aggiungere un account nuovo
            account = self.crea_account()
            self.db.aggiungi(account)
        elif scelta == "2":
            # modificare un account esistente
            self.modifica_account()
        elif scelta == "3":
            # eliminare un account esistente
            self.elimina_account()
        elif scelta == "4":
            self.db.stampa_db()

    def crea_account(self):
        print("\n Creazione nuovo account: \n")
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        data = input("Data: ")
        password = input("Password: ")
        account = {"nome" : nome, "cognome" : cognome, "data" : data, "password" : password}
        return account    

    def modifica_account(self):
        print("\n Modifica account: \n")
        self.db.stampa_db()
        indice = input("\nInserisci l'indice dell'account che si vuole modificare: ")
        try:
            indice = int(indice)
        except:
            print("errore: indice non numerico")
        print("Crea un nuovo account che rimpiazzerà quello selezionato")
        account = self.crea_account()
        self.db.rimpiazza(indice, account)

    def elimina_account(self):
        print("\n Elimina account: \n")
        self.db.stampa_db()
        indice = input("\nInserisci l'indice dell'account che si vuole modificare: ")
        try:
            indice = int(indice)
        except:
            print("errore: indice non numerico")        
        self.db.elimina(indice)
        print("account eliminato")


    def converti(self):
        print("Scegli un dizionario da convertire: ")
        self.db.stampa_db()
        indice = input("\nInserisci l'indice dell'account che si vuole modificare: ")
        try:
            indice = int(indice)
        except:
            print("errore: indice non numerico")
        formato = input("Scegli formato di conversione (json/pickle): ")
        if formato == "json":
            formato = json
        elif formato == "pickle":
            formato = pickle
        else:
            print("formato non valido")
            return
        dizio = self.db.database[indice]
        dizio_dump = formato.dumps(dizio)
        print(dizio_dump)

m = Menu()
m.start()
