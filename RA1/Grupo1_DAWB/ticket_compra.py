# Proyecto: Generador de ticket de compra
# Autores: David García Ramírez y Jesús Herrera Bailon

# Declaración de las constantes.
NOMBRE_TIENDA = "VP MARKET 24H"
IVA = 0.21
IVA_REDUCIDO = 0.04
PRESUPUESTO = 300

# Petición de los datos del cliente e introducción en variables.
print(f"Bienvenido a '{NOMBRE_TIENDA}'")
nombre_cliente = input("Introduce tu nombre: ")
nombre_producto = input("Introduce el nombre del producto: ")
precio_unidad = float(input("Introduce el precio por unidad: "))
cantidad = int(input("Introduce la cantidad de unidades comprada del producto: "))
porcentaje_descuento = float(input("Introduce el porcentaje de descuento (si no tiene ponga 0): "))
gastos_envio = float(input("Introduzca los gastos de envío si hubiera (si no, ponga 0): "))
anno = input("Introduce el año de la compra: ")
mes = input("Introduce el mes de la compra: ")
dia = input("Introduce el día de la compra: ")
fecha = dia + "/" + mes + "/" + anno

# Comprobación de tipos
print(f"""
---PRUEBAS DE TIPOS---
Nombre del cliente == str: {type(nombre_cliente) == str}
Nombre del producto == str: {type(nombre_producto)== str}
Precio de la unidad del producto == float: {type(precio_unidad) == float}
Cantidad del producto == int: {type(cantidad) == int}
Porcentaje de descuento del producto == float: {type(porcentaje_descuento) == float}
Gastos de envío == float: {type(gastos_envio) == float}
Fecha == str: {type(fecha) == str}
----------------------
""")

# Operaciones a realizar
subtotal = precio_unidad * cantidad
descuento = subtotal * (porcentaje_descuento/100)
base_postdescuento = subtotal - descuento + gastos_envio
importe_iva = base_postdescuento * IVA
importe_iva_reducido = base_postdescuento * IVA_REDUCIDO
total = base_postdescuento + importe_iva
total_reducido = base_postdescuento + importe_iva_reducido

# Comprobación de tipos de los resultados
print(f"""
---PRUEBAS DE TIPOS DE RESULTADOS---
Subtotal == float: {type(subtotal) == float}
Descuento == float: {type(descuento) == float}
Base después del descuento == float: {type(base_postdescuento) == float}
Importe del IVA == float: {type(importe_iva) == float}
Total == float: {type(total) == float}
Total reducido == float: {type(total_reducido) == float}
------------------------------------
""")

# Salida del Ticket
print(f"""
Nombre del cliente: {nombre_cliente}
Nombre del producto: {nombre_producto}
Precio por unidad: {precio_unidad:.2f}
Cantidad: {cantidad:d}
Descuento aplicado (%): {porcentaje_descuento:.2f}

========== TICKET DE COMPRA | {NOMBRE_TIENDA} ==========
Fecha: {fecha}

Cliente: {nombre_cliente}
Producto: {nombre_producto}
Precio por unidad: {precio_unidad:.2f}€
Cantidad: {cantidad:d}

Subtotal: {subtotal:.2f}€
Descuento: {descuento:.2f}€
IVA: {importe_iva:.2f}€/IVA reducido: {importe_iva_reducido:.2f}€
Gastos de envío: {gastos_envio:.2f}€


TOTAL: {total:.2f}€/{total_reducido:.2f}€

Supera el presupuesto: {total > PRESUPUESTO}/{total_reducido > PRESUPUESTO}


Gracias por su compra
======================================
""")
