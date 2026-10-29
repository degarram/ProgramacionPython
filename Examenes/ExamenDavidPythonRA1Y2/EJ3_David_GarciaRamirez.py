# Ejercicio 3
# Autor: David García Ramírez 2ºDAW B

# Creo una constante para el menú inicial en caso de querer modificarlo
MENU_INICIAL = """
CALCULADORA
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Potencia
6. Resto de división
7. Salir
"""

# Un bucle que hace que el programa continue a menos que el usuario indique lo contrario
while True:
    try:
        # Se pide la elección por pantalla al usuario
        eleccion = int(input(MENU_INICIAL).strip()) # Se quitan los posibles espacios de la entrada

        if eleccion == None: # Si el valor es nulo, se indica al usuario que elija una opción
            print("\nIntroduce una opción.")
            continue

    except ValueError: # En caso de que la elección no sea un número, salta error
        print("\nLa opción debe ser un valor numérico.")
        continue # El programa salta la iteración acual y muestra el menú de nuevo

    if eleccion == 7: # En caso de elegir 7, el programa finalizará
        print("\nPrograma finalizado.")
        break # Sale del bucle y finaliza el programa

    elif eleccion not in range(1,8): # En caso de poner un número que no esté entre las opciones, informar al usuario
        print("\nOpción no válida")
        continue # Y mostrar el menú de nuevo

    elif eleccion in range(1,7): # En caso de que se elija una opción de entre las viables, se procede con el programa
        resultado = 0 # Se inicializa la variable para el resultado de manera global (dentro del ámbito del condicional actual), para poder mostrarlo

        # Un segundo bucle para evitar repetir el menú cuando lo que fallan son los números de las operaciones
        while True:
            try:
                # Se piden los números con los que se realizará la operación
                numero1 = float(input("\nIntroduce el primer número: ").strip()) # Se eliminan los posibles espacios de la entrada
                numero2 = float(input("Introduce el segundo número: ").strip())

                if numero1 == None or numero2 == None: # En caso de que cualquiera de los dos números sea nulo, se pide al usuario de nuevo que los introduzca
                    print("\nDebes introducir dos números.")
                    continue

            except ValueError: # En caso de que alguno de los valores no sea numérico, salta error
                print("\nDebes introducir valores numéricos.")
                continue # Y se pide de nuevo que el usuario introduzca los números
            
            # Si el programa continúa con normalidad, se realiza la operación correspondiente a cada elección
            if eleccion == 1: # Suma
                resultado = numero1 + numero2

            elif eleccion == 2: # Resta
                resultado = numero1 - numero2

            elif eleccion == 3: # Multiplicación
                resultado = numero1 * numero2

            elif eleccion == 4: # División
                try:
                    resultado = numero1 / numero2
                except ZeroDivisionError: # Si el divisor (el segundo número) es 0, no se puede dividir y salta error
                    print("\nNo se puede dividir entre cero.")
                    continue # Se sale de la iteración actual y se piden de nuevo los números
            
            elif eleccion == 5: # Potencia
                resultado = numero1 ** numero2
            
            elif eleccion == 6: # Resto
                try:
                    resultado = numero1 % numero2
                except ZeroDivisionError: # Si el divisor (el segundo número) es 0, no se puede dividir y salta error
                    print("\nNo se puede dividir entre cero.")
                    continue # Se sale de la iteración actual y se piden de nuevo los números
            
            break # Si todo va bien en cualquier operación, se sale del bucle interno
        
        # Finalmente se muestra el resultado con dos decimales
        print(f"\nResultado: {resultado:.2f}")

        # El programa no finaliza, pues estámos dentro de un bucle superior y no se ha indicado que se salga del mismo, por lo que se repetirá una nueva iteración

# En caso de que el usuario haya elegido la opción de salir del programa, el mismo sí que finalizará
