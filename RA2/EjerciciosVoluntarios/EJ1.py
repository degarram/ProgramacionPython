# Pedimos la nota y la convertimos a número decimal.
nota = float(input("Introduce una nota entre 0 y 10: "))

# Comprobamos primero si la nota está fuera del intervalo permitido.
if nota < 0 or nota > 10:
    print("Error: la nota debe estar entre 0 y 10.")
# Las notas inferiores a 5 se consideran suspensos.
elif nota < 5:
    print("Suspenso")
# Las notas desde 5 hasta menos de 7 son aprobados.
elif nota < 7:
    print("Aprobado")
# Las notas desde 7 hasta menos de 9 son notables.
elif nota < 9:
    print("Notable")
# El resto de notas válidas son sobresalientes.
else:
    print("Sobresaliente")
