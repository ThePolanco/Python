secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

while secret_number != True:
    number = int(input("Adivina el numero secreto: "))
    if number != secret_number:
        
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!") 
    else:
        print(secret_number)
        print("¡Bien hecho, muggle! Eres libre ahora.")