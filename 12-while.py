numero = 0

while numero <= 10:
    print(numero)
    numero += 1 # Incremento para evitar un Loop infinito

# IF DENTRO DEL WHILE
while numero <= 10:
    if numero == 5:
        break
    else:
        print(numero)
    numero += 1