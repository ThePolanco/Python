lista = []
valor = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    lista.append(val)

while valor:
    valor = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            valor = True
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print("\nOrdenada:")
print(lista)


# Forma en la que python hace todo el trabajo mediante el metodo sort:
print("---------------------------------------")
my_list = [8, 10, 6, 2, 4] 
my_list.sort() 
print(my_list)

# Metodo para invertir la lista:
lst = [5, 3, 1, 2, 4]
print(lst)
lst.reverse()
print(lst)



