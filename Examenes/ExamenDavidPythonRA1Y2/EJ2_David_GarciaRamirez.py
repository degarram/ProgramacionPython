# Ejercicio 2
# Autor: David García Ramírez 2ºDAW B

# Bucle para que el programa repita la entrada de datos en caso de que algún error ocurra
while True:
    try:
        # Se le piden al usuario los dos números que se van a usar para la operación
        numero1 = int(input("Introduce el primer número: "))
        numero2 = int(input("Introduce el segundo número: "))
    except ValueError: # Se controla que las variables de los números tengan valores númericos
        print("Debes introducir valores numéricos.")
        continue # Se salta a la siguiente iteración del bucle en caso de que no sean valores numéricos

    try:
        # Se realiza la operación
        resultado = numero1 / numero2
    except ZeroDivisionError: # Se controla que el divisor no sea 0
        print("No se puede dividir entre cero.")
        # Se acaba la iteración del bucle sin salir del mismo, por lo que se vuelve a repetir
    else:
        # En caso de que todo salga bien, se muestra la operación con el resultado por pantalla
        print(f"{numero1} / {numero2} = {resultado}")
        break # Se sale del bucle, finalizando el programa
