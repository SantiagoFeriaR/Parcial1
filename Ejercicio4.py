def cajero():
    try:
        dinero_inicial = int(input("Ingrese el dinero disponible: "))
        
        """Aqui estamos verificando que el dinero disponible no sea negativo, 
        porque no tendría sentido tener saldo negativo."""
        if dinero_inicial < 0:
            print("No se acepta saldo negativo.")
            return

        retiro = int(input("Ingrese cuánto desea retirar: "))
        
        """Checamos que el valor del retiro no sea negativo, ya que no se permite retirar menos que cero"""
        if retiro < 0:
            print("Error: No se permiten valores negativos")
            return

        """Si el retiro es mayor que el dinero disponible, entonces no se puede realizar la operacion"""
        if retiro > dinero_inicial:
            print("Error: Fondos insuficientes")
            return

        restante = dinero_inicial - retiro
        print("Dinero restante:", restante)

    except ValueError:
        """Si el usuario ingresa algo que no es un numero, capturamos el error y mostramos un mensaje apropiado"""
        print("Error: Debe ingresar un número válido.")


cajero()
cajero()
cajero()
cajero()
cajero()
