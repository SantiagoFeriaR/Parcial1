def analizar_numeros(*args, **kwargs):
    """Recibe números y separa los pares de los impares."""
    pares = [n for n in args if n % 2 == 0]  # Filtra los números pares
    impares = [n for n in args if n % 2 != 0]  # Filtra los números impares

    print("Pares:", pares)
    print("Impares:", impares)

""" llamada a la funcion con una lista de numeros"""
analizar_numeros(7, 12, 19, 24, 31, 46, 53, 60)
