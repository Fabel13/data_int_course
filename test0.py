# Creare un sistema che prenda in input un dato e lo stampi dopo aver controllato che sia valido (no "", "0", "False")

input_value = input("Inserisci un valore: ")
if input_value and input_value!="False" and input_value!="0":
    print("Hai inseritio il valore: " + input_value)
else:
    print("Il valore inserito non è valido (\"\", \"0\", \"False\")")


# Creare una serie di input, inserirli in una lista e stamparli controllando che la lista intera abbia solo valori validi (no "", "0", "False")

lista = []
valore1 = input("Inserisci il primo valore: ")
valore2 = input("Inserisci il secondo valore: ")
valore3 = input("Inserisci il terzo valore: ")
lista.append(valore1)
lista.append(valore2)
lista.append(valore3)
print(lista)
if (valore1 and valore1!="False" and valore1!="0") and (valore2 and valore2!="False" and valore2!="0") and (valore3 and valore3!="False" and valore3!="0"):
    print("La lista contiene tutti valori validi")
else:
    print("La lista contiene almeno un valore non valido")


# Creare un sistema di domande e input che inseriscano e controllino i dati; se non sono corretti non verranno inseriti nella lista

lista = []
domanda1 = "Come ti chiami?"
domanda2 = "Quanti anni hai?"
domanda3 = "Come stai?"

input_value = input(domanda1)
if input_value and input_value!="False" and input_value!="0":
    lista.append(input_value)
else:
    print("Il valore inserito non è valido, non verrà inserito nella lista")

input_value = input(domanda2)
if input_value and input_value!="False" and input_value!="0":
    lista.append(input_value)
else:
    print("Il valore inserito non è valido, non verrà inserito nella lista")

input_value = input(domanda3)
if input_value and input_value!="False" and input_value!="0":
    lista.append(input_value)
else:
    print("Il valore inserito non è valido, non verrà inserito nella lista")

print(lista)
