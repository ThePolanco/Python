#Comprobación de que los valores estan o no estan en la lista
"""lista = [0, 3, 12, 8, 2]

print(5 in lista)
print(5 not in lista)
print(12 in lista)"""


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista_unica = []

for number in my_list:
    if number not in lista_unica:
        lista_unica.append(number)

print("La lista con elementos únicos:")
print(lista_unica)
