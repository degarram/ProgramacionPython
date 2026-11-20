# Intentamos leer los dos números y realizar la división.
try:
    # Convertimos las entradas a números decimales.
    primer_numero = float(input("Introduce el primer número: "))
    segundo_numero = float(input("Introduce el segundo número: "))
    # Dividimos el primer número entre el segundo.
    resultado = primer_numero / segundo_numero
# Capturamos el error cuando alguna entrada no es numérica.
except ValueError:
    print("Error: debes introducir valores numéricos.")
# Capturamos el error cuando el divisor es cero.
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
# Si no se produce ningún error, mostramos el resultado.
else:
    print(f"Resultado: {resultado}")
