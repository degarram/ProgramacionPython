# Pedimos un número entero al usuario.
numero = int(input("Introduce un número: "))

# Repetimos la operación con los multiplicadores del 1 al 10.
for multiplicador in range(1, 11):
    # Mostramos cada resultado de la tabla.
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
