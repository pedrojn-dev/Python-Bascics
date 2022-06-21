#Ejemplo con elif
ocupacion = 'Nada'

if ocupacion == 'Estudiante':
    print('Tienes 50% de Descuento')
elif ocupacion == 'Jubilado':
    print('Tienes 75% de descuento')
elif ocupacion == 'Desempleado':
    print('Tienes un 10% de descuento')
else:
    print('Debes pagar el 100%')