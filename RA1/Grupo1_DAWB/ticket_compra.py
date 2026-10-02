# Declaración de la constante IVA.
IVA = 0.21

# Petición de los datos del cliente e introducción en variables.
nombre_cliente = input("Introduce tu nombre: ")
nombre_producto = input("Introduce el nombre del producto: ")
precio_unidad = float(input("Introduce el precio por unidad: "))
cantidad = int(input("Introduce la cantidad de unidades comprada del producto: "))
porcentaje_descuento = float(input("Introduce el porcentaje de descuento (si no tiene pon 0): "))

# Comprobación de tipos
print(f"""
---PRUEBAS DE TIPOS---
Nombre del cliente: {type(nombre_cliente) == str}
Nombre del producto: {type(nombre_producto)== str}
Precio de la unidad del producto: {type(precio_unidad) == float}
Cantidad del producto: {type(cantidad) == int}
Porcentaje de descuento del producto: {type(porcentaje_descuento) == float}
----------------------
""")

# Operaciones a realizar
subtotal = precio_unidad * cantidad
descuento = subtotal * (porcentaje_descuento/100)
base_postdescuento = subtotal - descuento
importe_iva = base_postdescuento * IVA
total = base_postdescuento + importe_iva

# Comprobación de tipos de los resultados
print(f"""
---PRUEBAS DE TIPOS DE RESULTADOS---
Subtotal: {type(subtotal) == float}
Descuento: {type(descuento) == float}
Base después del descuento: {type(base_postdescuento) == float}
Importe del IVA: {type(importe_iva) == float}
Total: {type(total) == float}
------------------------------------
""")

# Salida del Ticket
print(f"""
Nombre del cliente: {nombre_cliente}
Nombre del producto: {nombre_producto}
Precio por unidad: {precio_unidad:f}
Cantidad: {cantidad:d}
Descuento aplicado (%): {porcentaje_descuento:.2f}

========== TICKET DE COMPRA ==========

Cliente: {nombre_cliente}
Producto: {nombre_producto}
Precio por unidad: {precio_unidad:.2f}€
Cantidad: {cantidad:d}

Subtotal: {subtotal:.2f}€
Descuento: {descuento:.2f}€
IVA: {importe_iva:.2f}€


TOTAL: {total:.2f}€


Gracias por su compra
======================================
""")
