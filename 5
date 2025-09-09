def total_productos(lista):
    return len(lista)

def precio_promedio(lista):
    if not lista:
        return 0
    total = sum(item['precio'] for item in lista)
    return total / len(lista)

def producto_mas_caro(lista):
    if not lista:
        return None, 0
    caro = max(lista, key=lambda x: x['precio'])
    return caro['nombre'], caro['precio']

def producto_mas_barato(lista):
    if not lista:
        return None, 0
    barato = min(lista, key=lambda x: x['precio'])
    return barato['nombre'], barato['precio']

def ordenar_por_precio(lista):
    return sorted(lista, key=lambda x: x['precio'], reverse=True)

def generar_reporte():
    productos = []

    while True:
        nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break

        try:
            precio = float(input(f"Ingrese el precio de {nombre}: "))
            productos.append({"nombre": nombre, "precio": precio})
        except ValueError:
            print("Error: Precio inválido. Intente de nuevo.")

    print("\n--- Reporte de Productos ---")
    print(f"Total de productos: {total_productos(productos)}")
    print(f"Precio promedio: ${precio_promedio(productos):.2f}")

    nombre_caro, precio_caro = producto_mas_caro(productos)
    print(f"Producto más caro: {nombre_caro} (${precio_caro})")

    nombre_barato, precio_barato = producto_mas_barato(productos)
    print(f"Producto más barato: {nombre_barato} (${precio_barato})")

    print("\nProductos ordenados por precio (de mayor a menor):")
    productos_ordenados = ordenar_por_precio(productos)
    for item in productos_ordenados:
        print(f"{item['nombre']} - ${item['precio']}")

generar_reporte()
