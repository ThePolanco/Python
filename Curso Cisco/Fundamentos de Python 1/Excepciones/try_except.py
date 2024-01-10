try:
    value = int(input('Ingresa un número natural: '))
    reciprocal = 1 / value
    print('El recíproco de', value, 'es', reciprocal)
except ValueError:
    print('Error: Debes ingresar un número válido.')
except ZeroDivisionError:
    print('Error: No se puede calcular el recíproco de 0.')
except Exception as e:
    print('Ocurrió un error no manejado:', e)
except:
    print('Ha sucedido algo extraño, ¡lo siento!')