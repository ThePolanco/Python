# Tambien llamadas rebanadas de listas
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Para eliminar fragmentos de la lista se utiliza la función "del"
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)