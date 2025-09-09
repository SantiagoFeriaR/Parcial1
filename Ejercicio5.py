def total_productos(lista):
    """Retorna la cantidad total de productos en la lista"""
    return len(lista)

def precio_promedio(lista):
    """Calcula y retorna el precio promedio de los productos"""
    if not lista:
        return 0  # Si la lista está vacía, devolvemos 0 para evitar división por cero
    total = sum(item['precio'] for item in lista)  # Sumamos todos los precios
    return total / len(lista)  # Promedio = total de precios / cantidad de productos

def producto_mas_caro(lista):
    """Devuelve el nombre y precio del producto más caro"""
    if not lista:
        return None, 0  # Si la lista está vacía, retornamos None y 0
    caro = max(lista, key=lambda x: x['precio'])  # Buscamos el producto con el precio más alto
    return caro['nombre'], caro['precio']

def producto_mas_barato(lista):
    """Devuelve el nombre y precio del producto más barato"""
    if not lista:
        return None, 0  # Si la lista está vacía, retornamos None y 0
    barato = min(lista, key=lambda x: x['precio'])  # Buscamos el producto con el precio más bajo
    return barato['nombre'], barato['precio']

def ordenar_por_precio(lista):
    """Ordena la lista de productos por precio, de mayor a menor"""
    return sorted(lista, key=lambda x: x['precio'], reverse=True)  # reverse=True para orden descendente

def generar_reporte():
    productos = []

    while True:
        """Pedimos al usuario que ingrese los productos hasta que escriba 'fin'"""
        nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break  # Si el usuario escribe 'fin', terminamos el ingreso de productos

        try:
            """Intentamos convertir el precio a un número flotante. Si no se puede, mostramos un error."""
            precio = float(input(f"Ingrese el precio de {nombre}: "))
            productos.append({"nombre": nombre, "precio": precio})  # Agregamos el producto a la lista
        except ValueError:
            print("Error: Precio inválido. Intente de nuevo.")  # Si el precio no es válido, pedimos otra vez

    print("\n--- Reporte de Productos ---")
    """Mostramos el total de productos, el precio promedio, el más caro y el más barato"""
    print(f"Total de productos: {total_productos(productos)}")
    print(f"Precio promedio: ${precio_promedio(productos):.2f}")

    nombre_caro, precio_caro = producto_mas_caro(productos)
    print(f"Producto más caro: {nombre_caro} (${precio_caro})")

    nombre_barato, precio_barato = producto_mas_barato(productos)
    print(f"Producto más barato: {nombre_barato} (${precio_barato})")

    print("\nProductos ordenados por precio (de mayor a menor):")
    """Ordenamos los productos por precio y los mostramos en orden descendente"""
    productos_ordenados = ordenar_por_precio(productos)
    for item in productos_ordenados:
        print(f"{item['nombre']} - ${item['precio']}")

# Llamamos la función para generar el reporte de productos
generar_reporte()
