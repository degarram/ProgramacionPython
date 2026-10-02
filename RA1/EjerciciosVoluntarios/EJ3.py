# Ejercicio 3. Precio con IVA:
# Solicitar al usuario el precio de un producto y mostrar el precio con IVA (21%).

# Definición de la constante para el IVA
IVA = 0.21

# Solicitud al usuario del precio del producto
precio = float(input("Introduce el precio del producto: "))

# Mostrar el precio con IVA
print(f"El precio del producto es {precio} y el precio con IVA es {precio * (1 + IVA):.2f}.")
