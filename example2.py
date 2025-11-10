continuar = True
nombres = ""
direccion = ""
telefono = ""
correo = ""
edad = ""
acerca = ""
imprimir = ""
ingresar = ""

while continuar: 
    nombres = print("1. Ingresa tu nombres y apellidos: ")
    direccion = print ("2. Ingresa tu direccion: ")
    telefono = print ("3. Ingresa tu telefono: ")
    correo = print ("4. Ingresa tu correo electronico: ")
    edad = print ("5. Ingresa tu edad: ")
    acerca = print ("6. Ingresa una breve descripcion acerca de ti: ")
    imprimir = input("¿Deseas imprimir la informacion ingresada? (si/no): ").lower()
    ingresar = input ("¿Deseas ingresar otra informacion? (si/no): ").lower()

    opcion = int(input ("Seleccione una opcion (1-8): "))
    if opcion == 1: 
        if nombres == "":
            nombre = input("Ingresa tu nombres y apellidos: ")
        else:
            print("tu nombre es {nombres}.")
    if opcion == 2:
        if direccion == "":
            direccion = input("Ingresa tu direccion: ")
        else:
            print("tu direccion es {direccion}.")  
    if opcion == 3:
        if telefono == "":
            telefono = input("Ingresa tu telefono: ")
        else:
            print("tu telefono es {telefono}.")
    if opcion == 4:
        if correo == "":
            correo = input("Ingresa tu correo electronico: ")
        else:
            print("tu correo electronico es {correo}.") 
    if opcion == 5:
        if edad == "":
            edad = input("Ingresa tu edad: ")
        else:
            print("tu edad es {edad}.") 
    if opcion == 6: 
        if acerca == "":
            acerca = input("Ingresa una breve descripcion acerca de ti: ")
        else:
            print("tu descripcion es {acerca}.")
    if opcion
    if imprimir == "si":