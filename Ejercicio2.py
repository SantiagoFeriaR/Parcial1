def impuestos(precio_base):
    """Calcula el precio con el 19% de impuesto aplicado."""
    return precio_base * 1.19  # Aplica el 19% de impuesto

suma_total = 0
numero_producto = 1

while numero_producto <= 3:
    entrada = input(f"Ingrese el precio del producto {numero_producto}: ")
    try:
        precio_ingresado = float(entrada)
        
        """Si el precio es negativo, le decimos al usuario que no puede ser así"""
        if precio_ingresado < 0:
            print("El precio no puede ser negativo. Intente de nuevo.")
            continue
        
        suma_total += impuestos(precio_ingresado)
        numero_producto += 1
    except ValueError:
        """Si la entrada no es un numero, mostramos un mensaje de error"""
        print("Entrada inválida. Por favor, ingrese un número válido.")

"""Mostramos el total con los impuestos calculados al final"""
print(f"\nEl total con impuesto es: {suma_total:.2f}")
