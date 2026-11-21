"""
Programa modular para analizar números enteros.

Permite:
- Comprobar si un número es par o impar.
- Determinar si es positivo, negativo o cero.
- Calcular su cuadrado.
- Calcular su factorial mediante iteración y recursividad.
- Sumar los números desde 1 hasta el número introducido.
- Ejecutar pruebas para comprobar las funciones.

Los cálculos se separan de la entrada y salida de información:
las funciones de cálculo devuelven resultados mediante return,
mientras que el programa principal los muestra mediante print.
"""


def es_par(numero):
    """
    Comprueba si un número entero es par.

    Un número es par cuando el resto de dividirlo entre 2 es cero.
    La función admite números positivos, negativos y el cero.

    Parámetros:
        numero (int): Número entero que se quiere comprobar.

    Retorna:
        bool: True si el número es par; False si es impar.

    Ejemplos:
        es_par(8) devuelve True.
        es_par(7) devuelve False.
        es_par(0) devuelve True.
    """
    # % calcula el resto de la división.
    # La comparación == devuelve directamente True o False.
    return numero % 2 == 0


def comprobar_signo(numero):
    """
    Determina si un número entero es positivo, negativo o cero.

    Parámetros:
        numero (int): Número entero cuyo signo se quiere conocer.

    Retorna:
        str: "positivo" si es mayor que cero, "negativo" si es menor
             que cero o "cero" si su valor es cero.

    Ejemplos:
        comprobar_signo(5) devuelve "positivo".
        comprobar_signo(-3) devuelve "negativo".
        comprobar_signo(0) devuelve "cero".
    """
    # Cada return termina la función y entrega el resultado.
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"


def calcular_cuadrado(numero):
    """
    Calcula el cuadrado de un número entero.

    Elevar un número al cuadrado equivale a multiplicarlo por sí mismo.

    Parámetros:
        numero (int): Número entero que se quiere elevar al cuadrado.

    Retorna:
        int: Cuadrado del número recibido.

    Ejemplos:
        calcular_cuadrado(3) devuelve 9.
        calcular_cuadrado(-4) devuelve 16.
        calcular_cuadrado(0) devuelve 0.
    """
    # ** es el operador de potencia de Python.
    return numero ** 2


def factorial_iterativo(numero):
    """
    Calcula el factorial de un entero no negativo mediante un bucle.

    El factorial de n es el producto de los enteros desde 1 hasta n.
    Por definición, el factorial de cero es 1.

    Parámetros:
        numero (int): Número entero mayor o igual que cero.

    Retorna:
        int: Factorial del número recibido.

    Errores:
        ValueError: Si el número es negativo.

    Ejemplos:
        factorial_iterativo(5) devuelve 120.
        factorial_iterativo(0) devuelve 1.
    """
    # Se valida el dato antes de comenzar el cálculo.
    if numero < 0:
        raise ValueError("No se puede calcular el factorial de un negativo.")

    # El acumulador empieza en 1 porque vamos a multiplicar.
    # Si empezase en 0, todos los productos serían cero.
    resultado = 1

    # range excluye el límite final; usamos numero + 1 para incluir numero.
    for valor in range(1, numero + 1):
        resultado *= valor  # Equivale a: resultado = resultado * valor.

    # Si numero es 0, el bucle no se ejecuta y se devuelve 1.
    return resultado


def factorial_recursivo(numero):
    """
    Calcula el factorial de un entero no negativo mediante recursividad.

    La función se llama a sí misma con un número cada vez menor:
        factorial(n) = n * factorial(n - 1)

    El caso base es factorial(0) = 1 y permite detener las llamadas.

    Parámetros:
        numero (int): Número entero mayor o igual que cero.

    Retorna:
        int: Factorial del número recibido.

    Errores:
        ValueError: Si el número es negativo.
        RecursionError: Si se supera el límite de llamadas recursivas
                        permitido por Python.

    Ejemplos:
        factorial_recursivo(5) devuelve 120.
        factorial_recursivo(0) devuelve 1.
    """
    # Se rechazan los negativos para evitar que las llamadas
    # se alejen del caso base en lugar de acercarse a él.
    if numero < 0:
        raise ValueError("No se puede calcular el factorial de un negativo.")

    # Caso base: termina la recursión.
    if numero == 0:
        return 1

    # Caso recursivo: reduce el problema en una unidad.
    # La multiplicación se completa cuando la llamada devuelve su resultado.
    return numero * factorial_recursivo(numero - 1)


def sumar_hasta(numero):
    """
    Calcula la suma de los enteros desde 1 hasta el número recibido.

    Incluye el número indicado en la suma. Para cero devuelve 0,
    ya que no hay términos que sumar. No admite números negativos.

    Parámetros:
        numero (int): Límite superior de la suma, mayor o igual que cero.

    Retorna:
        int: Resultado de sumar 1 + 2 + ... + numero.

    Errores:
        ValueError: Si el número es negativo.

    Ejemplos:
        sumar_hasta(5) devuelve 15.
        sumar_hasta(1) devuelve 1.
        sumar_hasta(0) devuelve 0.
    """
    if numero < 0:
        raise ValueError("La suma requiere un número mayor o igual que cero.")

    # El acumulador empieza en 0 porque vamos a sumar.
    total = 0

    # Recorre los enteros desde 1 hasta numero, ambos incluidos.
    for valor in range(1, numero + 1):
        total += valor  # Equivale a: total = total + valor.

    return total


def mostrar_menu():
    """
    Muestra por pantalla las operaciones disponibles.

    Esta función solo presenta el menú. La lectura y el tratamiento
    de la opción elegida se realizan en main.

    Parámetros:
        Ninguno.

    Retorna:
        None: No devuelve un resultado explícito.

    Efectos:
        Escribe las opciones del programa en la consola.
    """
    # \\n introduce un salto de línea para separar el menú anterior.
    print("\n--- ANALIZADOR DE NÚMEROS ENTEROS ---")
    print("1. Comprobar si el número es par")
    print("2. Comprobar si es positivo, negativo o cero")
    print("3. Calcular el cuadrado")
    print("4. Calcular el factorial mediante iteración")
    print("5. Calcular el factorial mediante recursividad")
    print("6. Calcular la suma desde 1 hasta el número")
    print("7. Ejecutar los casos de prueba")
    print("0. Salir")


def ejecutar_pruebas():
    """
    Comprueba las funciones con resultados conocidos y entradas erróneas.

    Incluye pruebas con números positivos, negativos y cero.
    También compara las dos versiones del factorial y comprueba
    que las operaciones rechazan los valores negativos cuando procede.

    Las comprobaciones utilizan assert. Debe ejecutarse Python
    en modo normal, sin la opción -O, que desactiva estas sentencias.

    Parámetros:
        Ninguno.

    Retorna:
        None: Muestra un mensaje si se superan todas las pruebas.

    Errores:
        AssertionError: Si alguna comprobación no se cumple.
    """
    # assert verifica una condición.
    # Si es falsa, lanza AssertionError y señala un fallo en la prueba.

    # --- Pruebas de paridad ---
    # "is True" e "is False" comprueban que se devuelve un booleano.
    assert es_par(8) is True
    assert es_par(7) is False
    assert es_par(0) is True
    assert es_par(-4) is True

    # --- Pruebas del signo ---
    assert comprobar_signo(5) == "positivo"
    assert comprobar_signo(-3) == "negativo"
    assert comprobar_signo(0) == "cero"

    # --- Pruebas del cuadrado ---
    assert calcular_cuadrado(-4) == 16
    assert calcular_cuadrado(0) == 0
    assert calcular_cuadrado(3) == 9

    # --- Pruebas del factorial ---
    # Se comprueban tanto un caso normal como el caso base.
    assert factorial_iterativo(0) == 1
    assert factorial_iterativo(5) == 120
    assert factorial_recursivo(0) == 1
    assert factorial_recursivo(5) == 120

    # Ambas versiones deben devolver el mismo resultado de 0 a 9.
    for numero in range(10):
        assert factorial_iterativo(numero) == factorial_recursivo(numero)

    # --- Pruebas de la suma ---
    assert sumar_hasta(5) == 15
    assert sumar_hasta(0) == 0
    assert sumar_hasta(1) == 1

    # --- Pruebas de rechazo de negativos ---
    # Se recorren las funciones sin ejecutarlas todavía.
    # En cada vuelta, "funcion" se refiere a una de ellas.
    for funcion in (factorial_iterativo, factorial_recursivo, sumar_hasta):
        error_detectado = False

        try:
            # Llama a la función actual con un valor no permitido.
            funcion(-3)
        except ValueError:
            # La función ha rechazado el dato como se esperaba.
            error_detectado = True

        # Si no se lanzó ValueError, la prueba debe fallar.
        assert error_detectado, "La función debería rechazar los negativos."

    # --- Prueba de entrada no numérica ---
    error_detectado = False

    try:
        # Simula la conversión de una entrada incorrecta del usuario.
        int("abc")
    except ValueError:
        error_detectado = True

    assert error_detectado, "La entrada 'abc' debería producir ValueError."

    # Solo se llega aquí si todas las comprobaciones se han superado.
    print("Todas las pruebas se han superado correctamente.")


def main():
    """
    Ejecuta el programa interactivo y coordina sus funciones.

    Muestra el menú repetidamente, valida la opción seleccionada,
    solicita un entero y muestra el resultado de la operación elegida.
    Finaliza cuando el usuario selecciona la opción 0.

    Parámetros:
        Ninguno.

    Retorna:
        None: Gestiona la interacción por consola.

    Errores controlados:
        ValueError: Entrada no convertible a entero o valor no permitido
                    por una operación.
        RecursionError: Exceso de llamadas en el factorial recursivo.

    Observaciones:
        Los fallos de las pruebas generan AssertionError y se dejan
        visibles para facilitar la detección de errores del programa.
    """
    # El menú se repite hasta que se ejecuta break.
    while True:
        mostrar_menu()

        # input devuelve texto.
        # strip elimina espacios al principio y al final de la entrada.
        opcion = input("Selecciona una opción: ").strip()

        # Se comprueba la salida antes de pedir un número.
        if opcion == "0":
            print("Programa finalizado.")
            break

        # Las pruebas no necesitan que el usuario introduzca un número.
        if opcion == "7":
            ejecutar_pruebas()
            continue  # Vuelve al inicio del bucle y muestra el menú.

        # Se descartan las opciones que no corresponden a operaciones.
        if opcion not in ("1", "2", "3", "4", "5", "6"):
            print("Opción no válida. Selecciona una opción del menú.")
            continue

        # Primer try-except: valida la entrada del usuario.
        try:
            numero = int(input("Introduce un número entero: "))
        except ValueError:
            # Por ejemplo, int("abc") o int("3.5") provocan este error.
            print("Error: debes introducir un número entero, por ejemplo, 5.")
            continue

        # Segundo try-except: controla los errores de las operaciones.
        try:
            if opcion == "1":
                # Se utiliza directamente el booleano devuelto.
                if es_par(numero):
                    print(f"El número {numero} es par.")
                else:
                    print(f"El número {numero} es impar.")

            elif opcion == "2":
                signo = comprobar_signo(numero)
                print(f"El número {numero} es {signo}.")

            elif opcion == "3":
                cuadrado = calcular_cuadrado(numero)
                print(f"El cuadrado de {numero} es {cuadrado}.")

            elif opcion == "4":
                resultado = factorial_iterativo(numero)
                print(f"Factorial iterativo: {numero}! = {resultado}")

            elif opcion == "5":
                resultado = factorial_recursivo(numero)
                print(f"Factorial recursivo: {numero}! = {resultado}")

            elif opcion == "6":
                resultado = sumar_hasta(numero)
                print(f"La suma desde 1 hasta {numero} es {resultado}.")

        except ValueError as error:
            # Muestra el mensaje asociado al error.
            # Por ejemplo, el rechazo de un negativo en el factorial.
            print(f"Error: {error}")

        except RecursionError:
            # Incluso con un caso base correcto, un número grande puede
            # necesitar más llamadas de las que Python permite.
            print("Error: el número supera el límite de recursión de Python.")
            print("Prueba con un número menor o utiliza el factorial iterativo.")


# Este bloque ejecuta main solo cuando se inicia este archivo directamente.
# Si se importa desde otro archivo, sus funciones quedan disponibles
# sin que se abra automáticamente el menú.
if __name__ == "__main__":
    main()