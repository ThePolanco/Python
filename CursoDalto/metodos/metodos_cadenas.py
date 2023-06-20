cadena1 = "Hola soy Jeison"
cadena2 = "Bienvenido"

resultado = dir(cadena1) #devuelve todos los metodos que se pueden implementar

#dato.metodo()
resultado = cadena1.upper() #upper convierte a MAYUSCULA
resultado = cadena1.lower() #convierte a minuscula
resultado = cadena1.capitalize() #Primera letra en mayuscula

resultado = cadena1.find("j") #Buscar una cadena en otra cadena, devuelve -1 cuando no encuentra algo.
resultado = cadena1.index("a") #Hace lo mismo, pero lanza una excepción en caso de que no encuentre algo.

resultado = cadena1.isnumeric() #Si es numerico devuelve true, de lo contrario false.
resultado = cadena1.isalpha() #Igualmente pero con datos alfanumericos.

resultado = cadena1.count("o") #Devuelve la cantidad de veces que coincida.
resultado = len(cadena1) #Cantidad de caracteres que tiene una cadena.

resultado = cadena1.startswith("H") #Verifica si comienza con:
resultado = cadena1.endswith("son") #Verfica si termina con: 

resultado = cadena1.replace("la","lo") #Reemplaza una parte de la cadena.
resultado = cadena1.split(" ") #Separar cadenas con la cadena que le demos.

print(resultado)