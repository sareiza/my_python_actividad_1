menu = 12000
bebida = 3000

print ("Bienvenido a nuestro nuestro restaurante")
print ("El menu del dia incluye: Carne de pescado, arroz con coco, ensalada")
orden = input("Desea ordenar el menu del dia? (si/no): ").lower()
if orden == "si":
    bbebida = input("Desea agregar bebida a su orden? (si/no): ").lower()
    if bbebida == "si":
        total = menu + bebida 
        print (f"El total a pagar es: {total + (total* 0.08)} pesos con IVA incluido")
    else:
        total = menu
        print (f"El total a pagar es: {total + (total* 0.08)} pesos con IVA incluido")
else:
    print("Gracias por visitarnos")