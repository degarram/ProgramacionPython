"""
Ejercicio 3: calculadora modular con funciones.
"""
def sumar(a: float, b: float) -> float:
    """Devuelve la suma de a y b."""
    return a + b

def restar(a: float, b: float) -> float:
    """Devuelve la resta de b a a."""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Devuelve el producto de a y b."""
    return a * b

def dividir(a: float, b: float) -> float:
    """
    Devuelve la division de a entre b.

    Errores:
        ZeroDivisionError: Si b es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")

    return a / b

def main() -> None:
    """
    Solicita dos numeros y una operacion, y muestra el resultado.

    Parametros:
        Ninguno.

    Retorna:
        None: Gestiona la entrada y salida por consola.
    """
    try:
        a = float(input("Primer numero: "))
        b = float(input("Segundo numero: "))
        operacion = input("Operacion (+, -, *, /): ").strip()

        if operacion == "+":
            resultado = sumar(a, b)
        elif operacion == "-":
            resultado = restar(a, b)
        elif operacion == "*":
            resultado = multiplicar(a, b)
        elif operacion == "/":
            resultado = dividir(a, b)
        else:
            print("Error: operacion no valida.")
            return

        print(f"\nResultado: {resultado:.2f}")
    except ValueError:
        print("Error: debes introducir valores numericos.")
    except ZeroDivisionError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
