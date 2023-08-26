#Para capturar la temperatura promedio tomando datos por hora las 24 horas del dia
temps = [[0.0 for h in range(24)] for d in range(31)]

#
# La matriz se actualiza aquí.
#

highest = -100.0
total = 0.0
 
# Para 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Temperatura promedio al mediodía:", average )

# Para tomar la temperatura mas alta registrada
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("La temperatura más alta fue:", highest)

# Registrar los dias mas calurosos
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "fueron los días calurosos.")