# Ejercicio 1
# Autor: David García Ramírez 2ºDAW B

# Se pide al usuario por pantalla que introduzca una temperatura en grados Celsius.
temperatura_celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Se calculan los grados Fahrenheit a los que equivalen la temperatura introducida por el usuario usando la fórmula F = C * 1.8 + 32.
temperatura_fahrenheit = temperatura_celsius * 1.8 + 32

# Se muestra por pantalla un mensaje mostrando la temperatura introducida por el usuario y su equivalente en grados Fahrenheit.
print(f"La temperatura has introducido es {temperatura_celsius} grados Celsius, que es igual a {temperatura_fahrenheit} grados Fahrenheit.")
