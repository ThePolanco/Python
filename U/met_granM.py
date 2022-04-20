from fractions import Fraction
from scipy.optimize import linprog 
import numpy as np

print("----------------------------------------------------------------------------------------------------------")
print("RESOLUCION EJERCICIO MEDIANTE EL METODO DE LA GRAN M")
print("----------------------------------------------------------------------------------------------------------")
print("PASO 1: Declarar la funcion objetivo(F.O)")
print("PASO 2: Declarar las restricciones")
print("PASO 3: Despejar ecuaciones y declarar variables de holgura o artificiales segun corresponda")
print("PASO 4: Organizacion de la matriz")
print("PASO 5: Resolucion de la matriz tomando numeros pivote hasta que la fila Z sea completamente negativa")
print("----------------------------------------------------------------------------------------------------------")

z = [4,1] #Declaramos los valores de la FO
F_des = [[-4,-3],[1,2]] #Declaramos los valores de las restricciones con desigualdades
F_resdes = [-6,4] #Declaramos los resultados de las restricciones
F_igu = [[3,1]] #Declaramos los valores de la funcion con =
F_resigu = [3] #Declaramos el resultado de la funcion con =

print("Sabiendo que la FO es:  4x1 + x2")
print("Las restricciones son: \n3x1 + x2 = 3\n4x1 + 3x2 ≥ 6\nx1 + 2x2 ≤ 4")
print("----------------------------------------------------------------------------------------------------------")

print("Para poder armar la matriz se deben agregar variables de Holgura(S) y variables artificiales(R)\nsegun la igualdad o desigualdad correspondiente")
print("Entonces: ")
print("FO = \nz - 4x1 - x2 - 100R1 - 0S1 - 100R2 - 0S2 = 0")
print("\nS.A = \n3x1 + x2 + R1 = 3\n4x1 + 3x2 - S1 + R2 ≥ 6\nx1 + 2x2 + S2 ≤ 4")
print("----------------------------------------------------------------------------------------------------------")

filas = 4 #Numero de filas que contiene la matriz
columnas = 8 #Numero de columnas que contiene la matriz

print("MATRIZ INICIAL") #Se imprimira la primera matriz mediante la libreria numpy
matriz = np.array([[1,-4,-1,-100,0,-100,0,0],
                   [0,3,1,1,0,0,0,3],
                   [0,4,3,0,-1,1,0,6],
                   [0,1,2,0,0,0,1,4]]).reshape(filas, columnas) #Ingreso de los datos de la matriz inicial
print(matriz)
print("----------------------------------------------------------------------------------------------------------")


res = linprog(z, F_des, F_resdes, F_igu, F_resigu, bounds = (0,None))

print(res)
print("----------------------------------------------------------------------------------------------------------")
print("MATRIZ FINAL") #Se imprimira la matriz final mediante la libreria numpy
matriz = np.array([[1,0,0,(-493/5),0,-100,(-1/5),(17/5)],
                   [0,1,0,(2/5),0,0,(-1/5),(2/5)],
                   [0,0,1,(-1/5),0,0,(3/5),(9/5)],
                   [0,0,0,1,1,-1,1,1]]).reshape(filas, columnas) #Ingreso de los datos de la matriz final
print(matriz)
print("----------------------------------------------------------------------------------------------------------")
print("Valor Optimo: ", Fraction(str(res.fun)).limit_denominator(), "\nx1 y x2: ", res.x)
print("----------------------------------------------------------------------------------------------------------")