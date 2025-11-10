precio = 25000
estudiante = 0.15
cupon = 0.10

print ("Bienvenido a la Libreria El Saber")
print ("donde todos nuestros libros cuestan 25000 pesos")
compra = input("Desea comprar un libro? (si/no): ").lower()
if compra == "si":
    es_estudiante_usuario = input("Es usted estudiante? (si/no): ").lower()
    if  es_estudiante_usuario == "si":
        tienec = input("Tiene cupon de descuento? (si/no): ").lower()
        if tienec == "si":
            ingrese_cupon = input("Ingrese el valor del cupon: ")
            if ingrese_cupon == "libro10":
                print ("El valor a pagar es ", precio - (precio * estudiante) - (precio * cupon))
                  
            else:
                total = precio - (precio * estudiante)
                print(f"El total a pagar es: {total} pesos")
        else:
            total = precio - (precio * estudiante)
            print(f"El total a pagar es: {total} pesos")
    else:
        total = precio
        print ("El valor a pagar es ", precio)
else:
    print("Gracias por visitarnos")
