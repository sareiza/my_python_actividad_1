pchocolate = 4000
pvainilla = 3500
ptopping = 1000

print ("Bienvenido a Frosty heladeria")
print('(sabores disponibles: chocolate, vainilla): ')
sabor = input("Ingrese el nombre del sabor: ").lower()
wantTopping = input("Desea agregar topping? (si/no): ").lower()

if sabor == "chocolate":
    if(wantTopping == "si"):
        total = (pchocolate ) + (ptopping )
        print(f"El total a pagar es: {total} pesos")
    else:
        total = pchocolate
        print(f"El total a pagar es: {total} pesos")

elif(sabor == "vainilla"):
        if(wantTopping == "si"):
            total = (pvainilla ) + (ptopping )
            print(f"El total a pagar es: {total} pesos")
        else:
            total = pvainilla
            print(f"El total a pagar es: {total} pesos")

else:
    print("Sabor no disponible")