# Proyecto: Laboratorio matemático modular
# Autores: Jesus Herrera Bailon y David Garcia Ramirez


# Si alguna falla, Python mostrará un AssertionError.

import operaciones

# ---------- PRUEBAS NORMALES ----------

# Caso 1: área
assert operaciones.calcular_area_rectangulo(5, 3) == 15
# Caso 2: perímetro
assert operaciones.calcular_perimetro_rectangulo(5, 3) == 16
# Área y perímetro con decimales
assert operaciones.calcular_area_rectangulo(2.5, 2) == 5.0
assert operaciones.calcular_perimetro_rectangulo(2.5, 2) == 9.0
# Caso 4: par
assert operaciones.es_par(8) is True
# Caso 5: impar
assert operaciones.es_par(7) is False
# Caso 7: factorial iterativo de 5
assert operaciones.factorial_iterativo(5) == 120
# Caso 8: factorial recursivo de 5
assert operaciones.factorial_recursivo(5) == 120

# ---------- PRUEBAS LÍMITE ----------

# Caso 6: factorial de 0 (tiene que dar 1)
assert operaciones.factorial_iterativo(0) == 1
assert operaciones.factorial_recursivo(0) == 1
# Factorial de 1
assert operaciones.factorial_iterativo(1) == 1
assert operaciones.factorial_recursivo(1) == 1
# El 0 es par
assert operaciones.es_par(0) is True
# Números negativos par/impar
assert operaciones.es_par(-4) is True
assert operaciones.es_par(-3) is False

# Los dos factoriales deben dar lo mismo
for n in range(0, 11):
    assert operaciones.factorial_iterativo(n) == operaciones.factorial_recursivo(n)

# ---------- PRUEBAS ERRÓNEAS ----------

# Caso 9: factorial de un negativo -> devuelve None (no se queda en bucle)
assert operaciones.factorial_iterativo(-3) is None
assert operaciones.factorial_recursivo(-3) is None

# ---------- PRUEBAS DEL HISTORIAL ----------

# La lista se modifica dentro de la función (es mutable)
historial = []
operaciones.registrar_resultado(historial, "prueba")
assert len(historial) == 1
assert historial[0] == "prueba"

print("Todas las pruebas han pasado correctamente.")

# ---------- PRUEBAS MANUALES (se hacen ejecutando main.py) ----------
# Caso 3:  opción 1, base 0 y altura 3  -> "Error: la base y la altura deben ser mayores que cero."
# Caso 9:  opción 3 o 4 con -3          -> "Error: el factorial no está definido para números negativos."
# Caso 10: escribir "cinco"             -> "Error: debes introducir un valor numérico." (ValueError)
# Caso 11: opción 5 sin operaciones     -> "El historial está vacío."
# Caso 12: opción 9                     -> "Opción no válida. Selecciona una opción del 1 al 6."
