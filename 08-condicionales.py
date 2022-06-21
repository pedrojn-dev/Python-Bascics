# Revisar si una condición es mayor a
balance = 500
if balance > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')

#Likes
likes = 200
if likes >= 200:
    print('Excelente, 200 Likes')
else: 
    print('Casi llegas a los 200')

# IF con texto
lenguaje = 'PHP'
if not lenguaje == 'Python':
    print ('Excelente decisión')

#Evaluar un Boolean
usuario_autenticado = True

if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')

# Evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'Javascript']

if 'PHP' in lenguajes:
    print('PHP Si existe')
else:
    print('No no esta en la lista')

#If Anidados
usuario_autenticado = False
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesión')
