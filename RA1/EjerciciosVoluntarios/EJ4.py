# Ejercicio 4. Conversión de temperatura:
# Solicitar al usuario una temperatura en grados Celsius y mostrarla en grados Fahrenheit.

# Solicitud al usuario de la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Conversión de Celsius a Fahrenheit
fahrenheit = celsius * 1.8 + 32

# Mostrar la temperatura en grados Fahrenheit
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")
