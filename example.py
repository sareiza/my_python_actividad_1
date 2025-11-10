while True:

   nombre = input("Ingresa tu nombre: ")
   edad = int(input("Ingresa tu edad: "))
   genero = input("Ingesa tu genero: ")

   print (f"tu nombres es: {nombre}, tu edad es: {edad}, tu genero es: {genero}.")
   continuar = input("¿Deseas continuar? (si/no): ").lower()
   if continuar != 'si':
    break