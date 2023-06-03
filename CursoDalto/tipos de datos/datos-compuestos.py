lista = ["Jeison Polanco", "ThePolanco", True, 1.67]
tupla = ("Jeison Polanco", "ThePolanco", True, 1.67)
#Las tuplas no se pueden modificar, mientras que las listas SI.

#Esto es valido
lista[3] = "Juan Andres"

#Esto no es valido
#tupla[3] = "Juan Andres"

#Creando un conjunto (set)
#En un conjunto no se mostraran datos duplicados
conjunto = {"Jeison Polanco", "ThePolanco", True, 1.67}

#print(conjunto[1]) = Esto no se puede hacer.

#Diccionario
#Key - value
diccionario = {
    'nombre' : "Jeison Polanco",
    'nickname' : "ThePolanco",
    'altura' : 1.67
}
print(diccionario['altura'])