# Iniciar un diccionario vacio
jugador = {}
print(jugador)

# Se une un jugador
jugador['nombre'] = 'Juan'
jugador['puntaje'] = 0
print(jugador)

# Incrementando el puntaje
jugador['puntaje']  = 100
print(jugador)

# Incrementando el puntaje
jugador['puntaje']  = 200
print(jugador)

# Acceder a un valor
print(jugador.get('consola', 'No existe ese valor'))

# Iterar en el diccionario
for llave, valor in jugador.items():
    print(valor)

# eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']
print(jugador)