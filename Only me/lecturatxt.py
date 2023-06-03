#w --> escribir
#a --> actualizar
#r --> lectura
nombre = input("Digite su nombre: ")
apellido = input("Digite su apellido: ")
f = open("nombres.txt","w")
f.write(nombre + '\n' + apellido)
f.close()

f = open("nombres.txt","r")
mensaje = f.read()
print(mensaje)
f.close()

