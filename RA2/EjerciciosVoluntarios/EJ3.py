# Inicializamos el acumulador de los números positivos.
suma_positivos = 0

# Solicitamos cinco números al usuario.
for i in range(5):
    # Convertimos cada entrada a un número decimal.
    numero = float(input("Introduce un número: "))

    # Los números negativos no se suman.
    if numero < 0:
        continue

    # Acumulamos únicamente los números positivos y el cero.
    suma_positivos += numero

# Mostramos la suma final.
print(f"Suma de los números positivos: {suma_positivos:g}")
