# Proyecto: Taquilla de cine
# Autores: David García Ramírez y Jesús Herrera Bailon

MENSAJE_MENU = """
========== TAQUILLA DE CINE ========== 
 
1. Vender entradas 
2. Consultar resumen de ventas 
3. Salir

"""
LIMITE_EDAD_INFANTIL = 5
LIMITE_EDAD_MENORES = 18
LIMITE_EDAD_SENIOR = 65
PRECIO_ENTRADA_INFANTIL = 0
PRECIO_ENTRADA_MENORES = 5
PRECIO_ENTRADA_GENERAL = 9
PRECIO_ENTRADA_SENIOR = 6

total_operaciones_realizadas = 0
total_entradas_vendidas = 0
total_dinero_recaudado = 0

while True:
    try:
        eleccion = int(input(MENSAJE_MENU))
    except ValueError:
        print("ERROR: Por favor, introduce un número entero válido para la elección.")
        continue

    if eleccion == 1:
        nombre_cli = input("\nIntroduce el nombre del cliente: ")
        edad_cli = 0
        nro_entradas = 0

        while True:
            try:
                edad_cli = int(input("Introduce la edad del cliente: "))
                if edad_cli < 0:
                    print("ERROR: La edad no puede ser negativa. Por favor, introduce un valor válido.")
                    continue
            except ValueError:
                print("ERROR: La edad debe ser un número entero válido.")
            else:
                break
        while True:
            try:
                nro_entradas = int(input("Introduce el número de entradas a comprar: "))
                if nro_entradas <= 0:
                    print("ERROR: El número de entradas no puede ser negativo. Por favor, introduce un valor válido.")
                    continue
            except ValueError:
                print("ERROR: El número de entradas debe ser un número entero válido.")
            else:
                break
        tipo_entrada = ""
        precio_entrada = 0
        total_entradas = 0
        if edad_cli < LIMITE_EDAD_INFANTIL:
            tipo_entrada = "Infantil"
            precio_entrada = PRECIO_ENTRADA_INFANTIL
            total_entradas = precio_entrada * nro_entradas
        elif edad_cli < LIMITE_EDAD_MENORES:
            tipo_entrada = "Menores"
            precio_entrada = PRECIO_ENTRADA_MENORES
            total_entradas = precio_entrada * nro_entradas
        elif edad_cli < LIMITE_EDAD_SENIOR:
            tipo_entrada = "General"
            precio_entrada = PRECIO_ENTRADA_GENERAL
            total_entradas = precio_entrada * nro_entradas
        else:
            tipo_entrada = "Senior"
            precio_entrada = PRECIO_ENTRADA_SENIOR
            total_entradas = precio_entrada * nro_entradas
        print(f"""
    Nombre del cliente: {nombre_cli:s}
    Edad del cliente: {edad_cli:d}
    Número de entradas: {nro_entradas:d}

    ========== TICKET ========== 
    Cliente: {nombre_cli:s} 
    Tipo: {tipo_entrada:s} 
    Precio por entrada: {precio_entrada:.2f} € 
    Número de entradas: {nro_entradas:d} 
    TOTAL: {total_entradas:.2f} € 
    ============================
    """)
        total_operaciones_realizadas += 1
        total_entradas_vendidas += nro_entradas
        total_dinero_recaudado += total_entradas
    elif eleccion == 2:
        print(f"""
    ========== RESUMEN DE VENTAS ========== 

    Operaciones realizadas: {total_operaciones_realizadas:d}
    Entradas vendidas: {total_entradas_vendidas:d}
    Recaudación total: {total_dinero_recaudado:.2f} €

    =======================================
    """)
    elif eleccion == 3:
        print("\nPrograma finalizado.\nGracias por utilizar la taquilla.")
        break
    else:
        print("ERROR: Debes introducir una de las opciones. Por favor, inténtalo de nuevo.")
