"""
Ejercicio 2: comprobacion de numeros pares e impares.
"""

def es_par(numero: int) -> bool:
    """
    Comprueba si un numero entero es par.

    Parametros:
        numero (int): Numero entero a comprobar.

    Retorna:
        bool: True si es par y False si es impar.
    """
    return numero % 2 == 0

def main() -> None:
    """
    Solicita un entero y muestra si es par o impar.

    Parametros:
        Ninguno.

    Retorna:
        None: Gestiona la entrada y salida por consola.
    """
    try:
        numero = int(input("Introduce un numero: "))

        if es_par(numero):
            print("El numero es par.")
        else:
            print("El numero es impar.")
    except ValueError:
        print("Error: debes introducir un numero entero.")

if __name__ == "__main__":
    main()
