'''numbers = [10, 5, 8, 2, 1]
print("Lista:", numbers)

numbers[0] = 111
print("Lista nueva:", numbers)

numbers[1] = numbers[4]
print("Lista nueva 2:", numbers)

print(numbers[0]) # Accediendo al primer elemento de la lista.

print("\nLongitud de la lista:", len(numbers))

del numbers[1]
print(len(numbers))
print(numbers)'''

'''
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
hat_list[2] = int(input("Ingresa el numero a reemplazar: "))
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[4]
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Longitud de la lista: ", len(hat_list))
print(hat_list)
'''
'''
# append - insert
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
numbers.insert(1, 333)
print(numbers)
'''
'''
my_list = [10, 1, 8, 3, 5, 10]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
'''



# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for _ in range(2):
    nuevo = input("Ingresa un miembro de la banda: ")
    beatles.append(nuevo)
print("Paso 3:", beatles)

# paso 4
del beatles[3]  # Eliminar "Stu Sutcliffe"
del beatles[3]  # Eliminar "Pete Best"
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Miembros de la banda Beatles:", beatles)
print("Los Fav", len(beatles))
