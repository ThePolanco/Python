import matplotlib.pyplot as plt
import pandas as pd

user = input("Digite su usuario: ")
print("Bienvenido" + user + "!")
info = ["Fecha", "Area", "Fresa", "Fresa pri. calidad"]
datos = pd.DataFrame(columns = info)

while True:
    print("1. Ingresar información")
    print("2. Buscar información por area o fecha")
    print("3. Graficar datos por area")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("Has elegido la opcion ingresar informacion")
        print("\nDigita los valores correspondientes: ")
        
        fecha = input("Digita el dia actual: ")
        area = int(input("Digita el area de cultivo(1,2,3 o 4): "))
        fresa = float(input("Digita la cantidad total de fresa recolectada en libras: "))
        fresaPri = float(input("Digita la cantidad total de fresa de primera calidad recolectada en libras: "))
        
        datos = datos.append({
            "Fecha": fecha, "Area" : area, "Fresa": fresa, "Fresa pri. calidad": fresaPri
        }, ignore_index = True)
        
        datos.to_csv("dataset.csv", index = False)
    
    elif opcion == "2":
        print("Has elegido la opcion buscar info. por area o fecha")
        print("1. Busqueda por area")
        print("2. Busqueda por fecha")
        print("3. Salir")
        
        opcion1 = input("Elige una opción: ")
        
        if opcion1 == "1":
            area = int(input("Digite el area a buscar: "))
            areaD = datos[datos["Area"] == area]
            print(areaD)
            
        elif opcion1 == "2":
            fecha = int(input("Digite la fecha a buscar: "))
            fechaD = datos[datos["Fecha"] == fecha]
            print(fechaD)
        
        else:
            print("ERROR!")
            
    elif opcion == "3":
        print("Has elegido la opcion graficar datos por area")
        print("1. 1")        
        print("2. 2")
        print("3. 3")
        print("4. 4")
        
        opcion2 = input("Digita el area a buscar: ")
        
        areaD = datos[datos["Area"] == area]
        info1 = areaD.groupby("Fecha").sum()
        
        plt.plot(info1.index, info1["Fresa"])
        plt.show()
        
    elif opcion == "4":
        break
        
    else:
        print("ERROR!")