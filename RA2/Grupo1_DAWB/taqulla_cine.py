# Proyecto: Taquilla de cine
# Autores: David García Ramírez y Jesús Herrera Bailon
# Aclaración sobre los descuentos: Se presupone que los descuentos no son acumulativos, es decir, si un cliente tiene derecho a más de un descuento, solo se aplicará el de mayor valor.

# Constante para mantener externalizado el mensaje del menú principal, facilitando su modificación futura.
MENSAJE_MENU = """
========== TAQUILLA DE CINE ========== 
 
1. Vender entradas 
2. Consultar resumen de ventas 
3. Reiniciar resumen de ventas
4. Salir

"""

# Constante para la palabra de cancelación de la compra, que permite al usuario salir del proceso de venta en cualquier momento.
PALABRA_CANCELAR = "cancelar"

# Constantes para los límites de edad de las categorías de entradas.
LIMITE_EDAD_INFANTIL = 5
LIMITE_EDAD_MENORES = 18
LIMITE_EDAD_SENIOR = 65

# Constantes para los nombres de los tipos de entradas según la categoría de edad.
TIPO_ENTRADA_INFANTIL = "Infantil"
TIPO_ENTRADA_MENORES = "Menor"
TIPO_ENTRADA_GENERAL = "General"
TIPO_ENTRADA_SENIOR = "Senior"

# Constantes para los precios de las entradas según la categoría de edad.
PRECIO_ENTRADA_INFANTIL = 0
PRECIO_ENTRADA_MENORES = 5
PRECIO_ENTRADA_GENERAL = 9
PRECIO_ENTRADA_SENIOR = 6

# Constante para el descuento en caso de comprar 5 o más entradas, expresado como porcentaje.
DESCUENTO_COMPRA_MAYOR = 10

# Constante para el número mínimo de entradas para aplicar el descuento por compra mayor.
MIN_ENTRADAS_DESCUENTO = 5

# Constante para el descuento en caso de tener carné de estudiante, expresado como porcentaje.
DESCUENTO_ESTUDIANTE = 15

# Constante para el número máximo de entradas que se pueden comprar en una sola operación.
MAX_ENTRADAS = 10

# Variables para los contadores y acumuladores del resumen de ventas.
total_operaciones_realizadas = 0
total_entradas_vendidas = 0
total_entradas_infantiles = 0
total_entradas_menores = 0
total_entradas_generales = 0
total_entradas_senior = 0
total_dinero_recaudado = 0

# Bucle principal: mantiene el programa activo hasta seleccionar «Salir».
while True:
    try:
        # Se solicita y valida que la opción del menú sea un número entero entre 1 y 4.
        eleccion = int(input(MENSAJE_MENU))
        if eleccion not in range(1, 5):
            print("\nERROR: Debes introducir una de las opciones. Por favor, inténtalo de nuevo.")
            continue
    except ValueError:
        print("\nERROR: Por favor, introduce un número entero válido para la elección.")
        continue

    # Opción 1: recopila los datos del cliente y registra una venta.
    if eleccion == 1:
        # Inicializa las variables para la venta actual.
        venta_cancelada = False # Variable usada en los bucles para poder salir del mismo y cancelar la venta si el usuario introduce la palabra de cancelación.
        nombre_cli = ""
        edad_cli = 0
        nro_entradas = 0
        descuento_aplicado = 0
        carné_estudiante = ""

        print("\nEscriba 'cancelar' en cualquier momento para cancelar la venta y volver al menú principal.\n")

        nombre_cli = input("Introduce el nombre del cliente: ")
        if nombre_cli.strip().lower() == PALABRA_CANCELAR:
            print("\nVenta cancelada. No se ha aplicado ningún cambio.")
            continue

        # Validación de la edad: debe ser un entero no negativo.
        while True:
            try:
                edad_introducida = input("Introduce la edad del cliente: ")
                if edad_introducida.strip().lower() == PALABRA_CANCELAR:
                    venta_cancelada = True
                    break
                edad_cli = int(edad_introducida)
                if edad_cli < 0:
                    print("\nERROR: La edad no puede ser negativa. Por favor, introduce un valor válido.")
                    continue
            except ValueError:
                print("\nERROR: La edad debe ser un número entero válido.")
            else:
                break

        if venta_cancelada:
            print("\nVenta cancelada. No se ha aplicado ningún cambio.")
            continue

        # Validación de la cantidad de entradas: debe ser un entero positivo e inferior al límite máximo {MAX_ENTRADAS}.
        while True:
            try:
                entradas_introducidas = input("Introduce el número de entradas a comprar: ")
                if entradas_introducidas.strip().lower() == PALABRA_CANCELAR:
                    venta_cancelada = True
                    break
                nro_entradas = int(entradas_introducidas)
                if nro_entradas <= 0:
                    print("\nERROR: El número de entradas debe ser un número entero positivo. Por favor, introduce un valor válido.")
                    continue
                if nro_entradas > MAX_ENTRADAS:
                    print(f"\nINFO: No se pueden comprar más de {MAX_ENTRADAS} entradas por operación. Por favor, introduce un valor menor.")
                    continue
            except ValueError:
                print("\nERROR: El número de entradas debe ser un número entero válido.")
            else:
                break

        if venta_cancelada:
            print("\nVenta cancelada. No se ha aplicado ningún cambio.")
            continue

        # Solicita al cliente si tiene carné de estudiante y valida la respuesta para asegurar que sea 's' o 'n'.
        while True:
            carné_estudiante = input("¿El cliente tiene carné de estudiante? (s/n): ").strip().lower()
            if carné_estudiante == PALABRA_CANCELAR:
                venta_cancelada = True
                break
            if carné_estudiante not in ["s", "n"]:
                print("\nERROR: Por favor, introduce 's' para Sí o 'n' para No.")
            else:
                break

        if venta_cancelada:
            print("\nVenta cancelada. No se ha aplicado ningún cambio.")
            continue

        # Determina la categoría y el precio según la edad del cliente y el precio total de la compra.
        tipo_entrada = ""
        precio_entrada = 0
        subtotal_compra = 0
        total_compra = 0
        if edad_cli < LIMITE_EDAD_INFANTIL:
            tipo_entrada = TIPO_ENTRADA_INFANTIL
            precio_entrada = PRECIO_ENTRADA_INFANTIL
            subtotal_compra = precio_entrada * nro_entradas
        elif edad_cli < LIMITE_EDAD_MENORES:
            tipo_entrada = TIPO_ENTRADA_MENORES
            precio_entrada = PRECIO_ENTRADA_MENORES
            subtotal_compra = precio_entrada * nro_entradas
        elif edad_cli < LIMITE_EDAD_SENIOR:
            tipo_entrada = TIPO_ENTRADA_GENERAL
            precio_entrada = PRECIO_ENTRADA_GENERAL
            subtotal_compra = precio_entrada * nro_entradas
        else:
            tipo_entrada = TIPO_ENTRADA_SENIOR
            precio_entrada = PRECIO_ENTRADA_SENIOR
            subtotal_compra = precio_entrada * nro_entradas

        # Aplica el descuento si se compran 5 o más entradas.
        if nro_entradas >= MIN_ENTRADAS_DESCUENTO:
            descuento_aplicado = DESCUENTO_COMPRA_MAYOR

        # Reemplaza el descuento por compra mayor si el cliente tiene carné de estudiante y este descuento es mayor.
        if carné_estudiante == "s" and descuento_aplicado < DESCUENTO_ESTUDIANTE:
            descuento_aplicado = DESCUENTO_ESTUDIANTE

        # Calcula el total después de aplicar el descuento correspondiente.
        if descuento_aplicado > 0:
            total_compra = subtotal_compra - (subtotal_compra * (descuento_aplicado / 100))
        else:
            total_compra = subtotal_compra

        # Muestra el ticket con los datos y el importe de la compra.
        print(f"""
    Nombre del cliente: {nombre_cli:s}
    Edad del cliente: {edad_cli:d}
    Número de entradas: {nro_entradas:d}

    ========== TICKET ==========
    Cliente: {nombre_cli:s}
    Tipo: {tipo_entrada:s}
    Precio por entrada: {precio_entrada:.2f} €
    Número de entradas: {nro_entradas:d}
    Subtotal: {subtotal_compra:.2f} €
    Descuento aplicado: {descuento_aplicado:d} %
    TOTAL: {total_compra:.2f} €
    ============================
    """)
        
        # Actualiza los acumuladores del resumen global después de completar la venta.
        total_operaciones_realizadas += 1
        total_entradas_vendidas += nro_entradas
        if tipo_entrada == TIPO_ENTRADA_INFANTIL:
            total_entradas_infantiles += nro_entradas
        elif tipo_entrada == TIPO_ENTRADA_MENORES:
            total_entradas_menores += nro_entradas
        elif tipo_entrada == TIPO_ENTRADA_GENERAL:
            total_entradas_generales += nro_entradas
        else:
            total_entradas_senior += nro_entradas
        total_dinero_recaudado += total_compra

    # Opción 2: muestra las estadísticas acumuladas de las ventas.
    elif eleccion == 2:
        # Variable para almacenar la media de recaudación por operación, evitando la división por cero si no se han realizado operaciones.
        media_recaudacion = 0
        if total_operaciones_realizadas > 0:
            media_recaudacion = total_dinero_recaudado / total_operaciones_realizadas

        print(f"""
    ========== RESUMEN DE VENTAS ========== 

    Operaciones realizadas: {total_operaciones_realizadas:d}
    Entradas tipo infantil vendidas: {total_entradas_infantiles:d}
    Entradas tipo menor vendidas: {total_entradas_menores:d}
    Entradas tipo general vendidas: {total_entradas_generales:d}
    Entradas tipo senior vendidas: {total_entradas_senior:d}
    Entradas vendidas: {total_entradas_vendidas:d}
    Media de recaudación por operación: {media_recaudacion:.2f} €
    Recaudación total: {total_dinero_recaudado:.2f} €

    =======================================
    """)
    # Opción 3: reinicia las estadísticas
    elif eleccion == 3:
        if input("\n¿Estás seguro de que deseas reiniciar el resumen de ventas? Esta acción no se puede deshacer. Introduce 'confirmar' en caso afirmativo: ").strip().lower() == "confirmar":
            total_operaciones_realizadas = 0
            total_entradas_vendidas = 0
            total_entradas_infantiles = 0
            total_entradas_menores = 0
            total_entradas_generales = 0
            total_entradas_senior = 0
            total_dinero_recaudado = 0
            print("Resumen de ventas reiniciado. Todos los contadores se han puesto a cero.\n")
        else:
            print("Reinicio cancelado. No se han aplicado cambios.")
    
    # Opción 4: finaliza el bucle y cierra el programa.
    elif eleccion == 4:
        print("\nPrograma finalizado.\nGracias por utilizar la taquilla.")
        break

# Fin del programa.
