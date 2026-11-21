"""
Ejercicio 5: cuenta atras mediante recursividad.
"""

def cuenta_atras(numero: int) -> None:
    """
    Imprime una cuenta atras desde numero hasta cero y despues "Fin".

    Parametros:
        numero (int): Numero entero no negativo desde el que comienza.

    Retorna:
        None: Es una funcion diseñada para mostrar salida.

    Errores:
        ValueError: Si numero es negativo.
    """
    if numero < 0:
        raise ValueError("La cuenta atras no admite numeros negativos.")

    if numero == 0:
        print("Fin")
    else:
        print(numero)
        cuenta_atras(numero - 1)

def main() -> None:
    """
    Solicita un numero entero y ejecuta la cuenta atras.

    Parametros:
        Ninguno.

    Retorna:
        None: Gestiona la entrada y salida por consola.
    """
    try:
        numero = int(input("Introduce un numero: "))
    except ValueError:
        print("Error: debes introducir un numero entero.")
        return

    try:
        print()
        cuenta_atras(numero)
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
