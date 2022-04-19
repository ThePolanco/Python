from fractions import Fraction
from scipy.optimize import linprog 

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

res = linprog(z, F_des, F_resdes, F_igu, F_resigu, bounds = (0,None))

print(res)
print("----------------------------------------------------------------------------------------------------------")
print("Valor Optimo: ", Fraction(str(res.fun)).limit_denominator(), "\nX1 y X2: ", res.x)
print("----------------------------------------------------------------------------------------------------------")