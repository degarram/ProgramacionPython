# Proyecto: Laboratorio matemático modular
# Autores: Jesus Herrera Bailon y David Garcia Ramirez

# Este archivo tiene las funciones que hacen los cálculos.
# No pide datos al usuario, solo recibe valores y devuelve resultados.


def calcular_area_rectangulo(base, altura):
    """Calcula y devuelve el área de un rectángulo."""
    area = base * altura
    return area


def calcular_perimetro_rectangulo(base, altura):
    """Calcula y devuelve el perímetro de un rectángulo."""
    perimetro = 2 * (base + altura)
    return perimetro


def es_par(numero):
    """Devuelve True si el número es par y False si es impar."""
    if numero % 2 == 0:
        return True
    else:
        return False


def factorial_iterativo(numero):
    """Calcula el factorial utilizando un bucle.
    Si el número es negativo devuelve None."""
    # El factorial no existe para negativos
    if numero < 0:
        return None
    resultado = 1
    # Multiplicamos desde 1 hasta el número
    for i in range(1, numero + 1):
        resultado = resultado * i
    # Si el número es 0, el bucle no se ejecuta y devuelve 1
    return resultado


def factorial_recursivo(numero):
    """Calcula el factorial mediante recursividad.
    Si el número es negativo devuelve None."""
    # Si es negativo paramos, así evitamos una recursión infinita
    if numero < 0:
        return None
    # Caso base: el factorial de 0 es 1
    if numero == 0:
        return 1
    # Caso recursivo: n! = n * (n - 1)!
    else:
        return numero * factorial_recursivo(numero - 1)


def registrar_resultado(historial, descripcion):
    """Añade una operación al historial."""
    # append modifica la lista original que nos pasan
    historial.append(descripcion)


def mostrar_historial(historial):
    """Muestra las operaciones almacenadas."""
    if len(historial) == 0:
        print("El historial está vacío.")
    else:
        print("\n========== HISTORIAL ==========")
        contador = 1
        for operacion in historial:
            print(str(contador) + ". " + operacion)
            contador = contador + 1
