#Creando una lista con list()
lista = list(["hola","Jeison",11])

#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#Agregar un elemento a la lista
agregar_append = lista.append("Bogotá")

#Agregar un elemento a la lista con un indice especifico
lista.insert(2, "Ola")

#Agregar varios elementos a la lista
lista.extend([False, 2023])

#Eliminar un elemento de la lista por su indice
lista.pop(2) #-1 para eliminar el ultimo, -2 para el antepenultimo y asi sucesivamente.

#Remover un elemento de la lista por su valor
lista.remove(False)

#Ordenar los elementos en orden numerico
#lista.sort()
#lista.sort(reverse = True) #Ordenar en forma descendente

#Invertir los elementos de una lista
lista.reverse()

#Eliminar todos los elementos de la lista
#lista.clear

print(lista)

#2:30:00