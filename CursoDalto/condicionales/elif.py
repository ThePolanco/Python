ingreso_mensual = 81000
gasto_mensual = 80000

#IF anidados y else if (elif)
if ingreso_mensual > 10000:
    if (ingreso_mensual - gasto_mensual) < 0:
        print("Estas en deficit economico")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien economicamente")   
    else:
        print("Estas gastando demasiado dinero")    

elif ingreso_mensual > 1000:
    print("Estas bien economicamente en LATAM")
    
else:
    print("Estas mal economicamente")