# Ejercicio 5. Datos de un rectángulo:
# Solicitar al usuario la base y la altura de un rectángulo y calcular su área y perímetro.

# Solicitud al usuario de la base y la altura del rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Cálculo del área y el perímetro del rectángulo
area = base * altura
perimetro = 2 * (base + altura)

# Mostrar el área y el perímetro del rectángulo
print(f"El área del rectángulo es: {area:.2f} y el perímetro es: {perimetro:.2f}")
