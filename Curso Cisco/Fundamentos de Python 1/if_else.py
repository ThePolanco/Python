# Si el ingreso del ciudadano no era superior a 85,528 pesos, 
# el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
# Si el ingreso era superior a esta cantidad, 
# el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.

# Debe aceptar un valor de punto flotante: el ingreso.
# A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. 
# Hay una función llamada round() que hará el redondeo por ti - la encontrarás en el código de esqueleto del editor.
# Nota: este país feliz nunca devuelve dinero a sus ciudadanos. 
# Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). 

# Observa el código en el editor - solo lee un valor de entrada y genera un resultado, 
# por lo que debes completarlo con algunos cálculos inteligentes.

ingreso = float(input("Ingresa el valor de tus ingresos: "))

if ingreso <= 85528:
    impuesto = ingreso * 0.18 - 556.02

else:
    impuesto = (ingreso - 85528) * 0.32 + 14839.02 
   
if impuesto < 0:
    impuesto = 0    

impuesto = round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")
    
