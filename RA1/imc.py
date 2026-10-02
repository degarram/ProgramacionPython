# Aquí se recogen las entradas de datos.
nombre = input("Introduce tu nombre: ")
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

# Calculamos el IMC (Índice de Masa Corporal).
imc = peso/altura**2

# Mostramos los resultados por pantalla con 2 decimales.
print(f"Hola {nombre}, tu peso es de {peso:.2f}kg y tu altura es de {altura:.2f}m, lo que indica que tu IMC es de {imc:.2f}.")
