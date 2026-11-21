"""
Ejercicio 1: area y perimetro de un rectangulo.
"""

def calcular_area(base: float, altura: float) -> float:
    """
    Calcula el area de un rectangulo.

    Parametros:
        base (float): Medida de la base.
        altura (float): Medida de la altura.

    Retorna:
        float: Producto de la base por la altura.

    Errores:
        ValueError: Si la base o la altura son negativas.
    """
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura no pueden ser negativas.")

    return base * altura

def calcular_perimetro(base: float, altura: float) -> float:
    """
    Calcula el perimetro de un rectangulo.

    Parametros:
        base (float): Medida de la base.
        altura (float): Medida de la altura.

    Retorna:
        float: Doble de la suma de la base y la altura.

    Errores:
        ValueError: Si la base o la altura son negativas.
    """
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura no pueden ser negativas.")

    return 2 * (base + altura)

def main() -> None:
    """
    Solicita las medidas y muestra el area y el perimetro.

    Parametros:
        Ninguno.

    Retorna:
        None: Gestiona la entrada y salida por consola.
    """
    try:
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
    except ValueError:
        print("Error: debes introducir valores numericos.")
        return

    try:
        area = calcular_area(base, altura)
        perimetro = calcular_perimetro(base, altura)

        print(f"Area: {area:.2f}")
        print(f"Perimetro: {perimetro:.2f}")
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
