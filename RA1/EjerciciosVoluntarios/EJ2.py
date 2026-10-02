# Ejercicio 2. Operaciones con dos números:
# Solicitar al usuario dos números y mostrar la suma, resta, multiplicación y división de ambos.

# Solicitud al usuario de dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Mostrar los resultados de las operaciones matemáticas
print(f"""
Los números son {num1:.2f} y {num2:.2f}.
Su suma es: {num1 + num2:.2f}
Su resta es: {num1 - num2:.2f}
Su multiplicación es: {num1 * num2:.2f}
Su división es: {num1 / num2:.2f}
""")
