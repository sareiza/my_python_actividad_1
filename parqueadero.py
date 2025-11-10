print ("Bienvenido a nuestro Parqueadero")
print ("Tarifa por hora: 2000 pesos durante las primeras 5 horas o fraccion de esta, luego de las 5 horas se cobra multa por 5000 mas las horas que siga ocupando el estacionamiento")
pago = input ("Desea realizar el pago ahora? (si/no): ").lower()
if pago == "si":
    print ("Recuerde que una fraccion de hora cueta como hora completa")
    horas = int (input ("Ingrese el numero de horas que estuvo estacionado: "))
    if horas < 0:
        print ("Numero de horas invalido")

    elif horas <= 5:
        total = horas * 2000
        print (f"El total a pagar es: {total} pesos")

    elif horas > 5: 
        print ("El valor a pagar es ", horas * 2000 + 5000)

    else:
        total = (5 * 2000) + 5000 + ((horas - 5) * 2000)
        print (f"El total a pagar es: {total} pesos")
