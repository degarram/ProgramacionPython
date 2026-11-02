# Proyecto: Taquilla de cine
# Autores: David García Ramírez y Jesús Herrera Bailon
# Aclaración sobre los descuentos: Se presupone que los descuentos no son acumulativos, es decir, si un cliente tiene derecho a más de un descuento, solo se aplicará el de mayor valor.

# Constante para el mensaje del menú principal
MENSAJE_MENU = """
╔════════════════════════════════════════════╗
║             TAQUILLA DE CINE               ║
╚════════════════════════════════════════════╝
╔════════════════════════════════════════════╗
     1. Vender entradas 
     2. Consultar resumen de ventas 
     3. Reiniciar resumen de ventas
     4. Salir
╚════════════════════════════════════════════╝
Selecciona una opción: """

# Constante para la palabra de cancelación de la compra
PALABRA_CANCELAR = "cancelar"

# Constantes para los límites de edad de las categorías de entradas
LIMITE_EDAD_INFANTIL = 5
LIMITE_EDAD_MENORES = 18
LIMITE_EDAD_SENIOR = 65

# Constantes para los nombres de los tipos de entradas
TIPO_ENTRADA_INFANTIL = "Infantil gratuita"
TIPO_ENTRADA_MENORES = "Menores"
TIPO_ENTRADA_GENERAL = "General"
TIPO_ENTRADA_SENIOR = "Sénior"

# Constantes para los precios de las entradas
PRECIO_ENTRADA_INFANTIL = 0.0
PRECIO_ENTRADA_MENORES = 5.0
PRECIO_ENTRADA_GENERAL = 9.0
PRECIO_ENTRADA_SENIOR = 6.0

# Constantes para los descuentos (ampliación voluntaria)
DESCUENTO_COMPRA_MAYOR = 10
MIN_ENTRADAS_DESCUENTO = 5
DESCUENTO_ESTUDIANTE = 15
MAX_ENTRADAS = 10

# Variables para contadores y acumuladores
total_operaciones_realizadas = 0
total_entradas_vendidas = 0
total_entradas_infantiles = 0
total_entradas_menores = 0
total_entradas_generales = 0
total_entradas_senior = 0
total_dinero_recaudado = 0.0

# Bucle principal: mantiene activo el menú
while True:
    try:
        opcion_input = input(MENSAJE_MENU)
        eleccion = int(opcion_input)
    except ValueError:
        print("\nError: debes introducir un número entero.")
        continue

    # Estructura if-elif-else para procesar las opciones del menú
    if eleccion == 1:
        venta_cancelada = False
        nombre_cli = ""
        edad_cli = 0
        nro_entradas = 0
        descuento_aplicado = 0
        carne_estudiante = ""

        print("\n(Escriba 'cancelar' en cualquier momento para cancelar la venta y volver al menú principal)\n")

        nombre_cli = input("Nombre del cliente: ")
        if nombre_cli.strip().lower() == PALABRA_CANCELAR:
            print("\nVenta cancelada. No se ha aplicado ningún cambio.")
            continue

        # Validación de la edad (bucle + try-except ValueError + comprobación negativa)
        while True:
            try:
                edad_introducida = input("Edad del cliente: ")
                if edad_introducida.strip().lower() == PALABRA_CANCELAR:
                    venta_cancelada = True
                    break
                edad_cli = int(edad_introducida)
                if edad_cli < 0:
                    print("Error: la edad no puede ser negativa.")
                    continue
                break
            except ValueError:
                print("Error: debes introducir un número entero.")

        if venta_cancelada:
            print("\nVenta cancelada. No se ha aplicado ningún cambio.")
            continue

        # Validación del número de entradas
        while True:
            try:
                entradas_introducidas = input("Número de entradas: ")
                if entradas_introducidas.strip().lower() == PALABRA_CANCELAR:
                    venta_cancelada = True
                    break
                nro_entradas = int(entradas_introducidas)
                if nro_entradas <= 0:
                    print("Error: el número de entradas debe ser mayor que cero.")
                    continue
                if nro_entradas > MAX_ENTRADAS:
                    print(f"Error: no se pueden comprar más de {MAX_ENTRADAS} entradas por operación.")
                    continue
                break
            except ValueError:
                print("Error: debes introducir un número entero.")

        if venta_cancelada:
            print("\nVenta cancelada. No se ha aplicado ningún cambio.")
            continue

        # Pregunta carné de estudiante (ampliación)
        while True:
            carne_estudiante = input("¿El cliente tiene carné de estudiante? (s/n): ").strip().lower()
            if carne_estudiante == PALABRA_CANCELAR:
                venta_cancelada = True
                break
            if carne_estudiante not in ["s", "n"]:
                print("Error: introduce 's' para Sí o 'n' para No.")
            else:
                break

        if venta_cancelada:
            print("\nVenta cancelada. No se ha aplicado ningún cambio.")
            continue

        # Estructura de selección con condiciones compuestas (and)
        tipo_entrada = ""
        precio_entrada = 0.0

        if edad_cli < LIMITE_EDAD_INFANTIL:
            tipo_entrada = TIPO_ENTRADA_INFANTIL
            precio_entrada = PRECIO_ENTRADA_INFANTIL
        elif edad_cli >= LIMITE_EDAD_INFANTIL and edad_cli < LIMITE_EDAD_MENORES:
            tipo_entrada = TIPO_ENTRADA_MENORES
            precio_entrada = PRECIO_ENTRADA_MENORES
        elif edad_cli >= LIMITE_EDAD_MENORES and edad_cli < LIMITE_EDAD_SENIOR:
            tipo_entrada = TIPO_ENTRADA_GENERAL
            precio_entrada = PRECIO_ENTRADA_GENERAL
        else:
            tipo_entrada = TIPO_ENTRADA_SENIOR
            precio_entrada = PRECIO_ENTRADA_SENIOR

        # Cálculo del subtotal
        subtotal_compra = precio_entrada * nro_entradas

        # Descuentos aplicables
        if nro_entradas >= MIN_ENTRADAS_DESCUENTO:
            descuento_aplicado = DESCUENTO_COMPRA_MAYOR

        if carne_estudiante == "s" and descuento_aplicado < DESCUENTO_ESTUDIANTE:
            descuento_aplicado = DESCUENTO_ESTUDIANTE

        # Total con descuento aplicado
        if descuento_aplicado > 0:
            total_compra = subtotal_compra - (subtotal_compra * (descuento_aplicado / 100))
        else:
            total_compra = subtotal_compra

        # Ticket con salidas económicas formateadas a dos decimales
        precio_str = f"{precio_entrada:.2f} €"
        subtotal_str = f"{subtotal_compra:.2f} €"
        descuento_str = f"{descuento_aplicado:d} %"
        total_str = f"{total_compra:.2f} €"

        print(f"""
 ╔════════════════════════════════════════════════════════╗
 ║                   TICKET DE COMPRA                     ║
 ╚════════════════════════════════════════════════════════╝
    Cliente        : {nombre_cli:<31s} 
    Tipo           : {tipo_entrada:<31s} 
    Precio/Entrada : {precio_str:<31s} 
    Nº Entradas    : {nro_entradas:<31d} 
  ════════════════════════════════════════════════════════
    Subtotal       : {subtotal_str:<31s}  
    Descuento      : {descuento_str:<31s}  
  ════════════════════════════════════════════════════════
    TOTAL          : {total_str:<31s}  
 ╚════════════════════════════════════════════════════════╝
        """)

        # Actualización de contadores y acumuladores
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

    # Opción 2: Resumen de ventas
    elif eleccion == 2:
        media_recaudacion = 0.0
        if total_operaciones_realizadas > 0:
            media_recaudacion = total_dinero_recaudado / total_operaciones_realizadas

        print(f"""
  ╔════════════════════════════════════════════════════════╗
  ║                   RESUMEN DE VENTAS                    ║
  ╚════════════════════════════════════════════════════════╝
    Operaciones realizadas: {total_operaciones_realizadas:d}
    Entradas vendidas: {total_entradas_vendidas:d}
      - Infantiles: {total_entradas_infantiles:d}
      - Menores:    {total_entradas_menores:d}
      - Generales:  {total_entradas_generales:d}
      - Sénior:     {total_entradas_senior:d}
    Recaudación total: {total_dinero_recaudado:.2f} €
    Media por operación: {media_recaudacion:.2f} €
  ╚════════════════════════════════════════════════════════╝
        """)

    # Opción 3: Reiniciar estadísticas (ampliación)
    elif eleccion == 3:
        confirmacion = input("\nIntroduce 'confirmar' para reiniciar las estadísticas: ").strip().lower()
        if confirmacion == "confirmar":
            total_operaciones_realizadas = 0
            total_entradas_vendidas = 0
            total_entradas_infantiles = 0
            total_entradas_menores = 0
            total_entradas_generales = 0
            total_entradas_senior = 0
            total_dinero_recaudado = 0.0
            print("Resumen de ventas reiniciado con éxito.\n")
        else:
            print("Operación cancelada. No se han modificado los datos.\n")

    # Opción 4: Salir del programa con break
    elif eleccion == 4:
        print("\nPrograma finalizado.\nGracias por utilizar la taquilla.")
        break

    # Opción no válida: control exigido en rúbrica con continue
    else:
        print("\nOpción no válida. Selecciona una opción del 1 al 4.")
        continue

# Fin del programa.
