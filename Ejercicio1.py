def numeropositivo():
    try:
        """Pedimos al usuario un número entero positivo para hacer las tablas de multiplicar"""
        num = int(input("Digite un número entero positivo: "))
        
        """Si el número es negativo o 0, decimos que no vale y salimos de la función"""
        if num <= 0:
            print("Error: El número debe ser un entero positivo. Intente de nuevo.")
            return  # Aquí ya no seguimos con el resto de la función, porque el número no sirve
        
        tabla = 0  # Vamos a guardar qué tabla tuvo el resultado más largo
        longitud_mas_larga = 0  # Esta variable va a medir cuántos dígitos tiene la tabla más larga
        
        """Empezamos a generar las tablas de multiplicar, una por cada número hasta 'num'"""
        for i in range(1, num + 1):
            """Generamos la tabla de multiplicar del número 'i', multiplicando del 1 al 10"""
            for j in range(1, 11):
                print(f"{i} x {j} = {i * j}")  # Imprimimos la multiplicación
            
            """Calculamos el resultado más grande de la tabla, que es i * 10"""
            resultado_maximo = i * 10

            cantidad_digitos = len(str(resultado_maximo))
            
          
            if cantidad_digitos > longitud_mas_larga:
                longitud_mas_larga = cantidad_digitos
                tabla = i  # Guardamos qué número tiene la tabla más larga en cuanto a dígitos
            
            print()  
        
        """Al final, mostramos cuál de las tablas tuvo los resultados más largos"""
        print(f"La tabla más larga fue la del número {tabla}.")
    
    except ValueError:
        """Si el usuario no ingresa un número válido, le avisamos del error"""
        print("Error: Ingreso no válido. Debe ser un número entero positivo.")

# Ejecutamos la función
numeropositivo()
numeropositivo()
numeropositivo()
