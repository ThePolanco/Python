from cmath import e, pi
from tkinter import E
from fractions import Fraction

"""numero = 2

print(pi+numero)"""

"""Operadores lógicos"""

"""x = True
y = False
print(x or y)
print(x and y)
print(not x)"""

"""Operadores de comparacion"""
"""x = 9
print(1 < x or x < 8)"""

"""Operadores Aritméticos"""
"""x = 5
y = 2
print(x + y) #Suma
print(x - y) #Resta
print(x * y) #Producto
print(x / y) #Division
print(x % y) #Resto
print(x // y) #Cociente
print(x ** y) #Potencia"""

"""Operadores a nivel de bits
Supongamos que tenemos el entero 2(en bits 00010)
y el entero 7(00111)"""
"""x = 2
y = 7
print(x | y)
print(x ^ y)
print(x & y)
print(x << 1)
print(x >> 1)
print(~x)"""

"""Operadores de asignación"""
"""x=2
x += 2
print(x)"""

"""Operadores de pertenencia"""
"""lista = [1,2,6,3,4,9,7]
print(4 in lista)
print(10 in lista)
print(3 not in lista)"""

"Operadores de identidad"
"""x = 4
y = 2
lista = [4,6,8]
print(x is lista)
print(x is y)
print(x is 4)"""

"If elif else"
"""x = 30
if x < 0:
    print(f'{x} es menor que 0')
elif x > 0:
    print(f'{x} es mayor que 0')
else:
    print('x es 0')"""
    
"If anidados"
"""x = 0
if x < 0:
    print(f'{x} es menor que 0')
else:
    if x > 0:
        print(f'{x} es mayor que 0')
    else:
        print('x es 0')"""

"While"
"""numero = 0
print('Tabla del 3')
while numero <= 10:
    print(f'{numero * 3}')
    numero += 1
print('Fin')"""

"While con break"
"""valores = [5, 1, 9, 2, 7, 4]

indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        print(f'El elemento 2 ha sido encontrado en el índice {indice}')
        break
    else:
        indice += 1
else:
    print('El elemento 2 no se encuentra en la lista de valores')"""