edad = int(input("Ingrese su edad: "))

if edad < 5:
    print("Tu entrada es gratuita.")
elif edad < 18:
    print("Tu entrada es de 5 euros.")
elif edad < 65:
    print("Tu entrada es de 10 euros.")
else:
    print("Tu entrada es de 6 euros")
