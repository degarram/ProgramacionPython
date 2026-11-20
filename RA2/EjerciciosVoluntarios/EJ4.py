# Guardamos el número que el usuario debe adivinar.
NUMERO_SECRETO = 7

# Repetimos las preguntas hasta que el usuario acierte.
while True:
    # Pedimos un número entero al usuario.
    numero = int(input("Adivina el número secreto: "))

    # Indicamos que el número secreto es mayor si el intento es menor.
    if numero < NUMERO_SECRETO:
        print("El número secreto es mayor")
    # Indicamos que el número secreto es menor si el intento es mayor.
    elif numero > NUMERO_SECRETO:
        print("El número secreto es menor")
    # Si no es menor ni mayor, el usuario ha acertado.
    else:
        print("¡Has acertado!")
        # Terminamos el bucle después de acertar.
        break
