#pedir al usuario que ingrese una palabra.
#utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas;
#hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes
#utiliza la ejecución condicional y la instrucción continue para "devorar" 
#las siguientes vocales A, E, I, O, U de la palabra ingresada.
#imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada

"""word_without_vowels = ""

user_word = input("Escribe una palabra: ")

user_word = user_word.upper()

for letter in user_word:
        if letter in "AEIOU":
            continue
        
        word_without_vowels += letter
        
print("Palabra sin vocales: ")
print(word_without_vowels)"""

"""blocks = int(input("Ingresa el número de bloques: "))

height = 0
blocks_used = 0

while blocks_used <= blocks:
    height += 1
    blocks_in_layer = height
    blocks_used += blocks_in_layer

print("La altura de la pirámide:", height - 1)"""


c0 = float(input("Ingresa un numero entero a excepcion de - y 0: "))

if c0 % 2 == 0:
    c0 /= 2
    print(c0)
elif c0 % 2 == 1:
    c0 = 3 * c0 + 1
    print(c0)
if c0 != 1:                     
    print(c0)