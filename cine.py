while True:
    print ("¡Bienvenido al Cine la Estrella!, el dia de hoy tenemos en Cartelera Penurias en Riwi")
    respuesta = input ("Deseas comprar una boleta?: S/N: ").lower()
    if respuesta == "s":
        cuantos_boletos = input ("¿Desea comprar uno o varios boletos?: 1/varios: ").lower()
        if cuantos_boletos == "1":
            edad = int(input ("Por favor ingresa tu edad: "))
            if edad < 0:
                print ("Edad invalida, por favor ingresa una edad correcta")
                continue
            if edad < 5:
                print ("El valor de la boleta es gratis")
                confirmacion = input ("¿Deseas confirmar tu boleta gratis?: S/N: ").lower()
                if confirmacion == "s":
                    print ("Boleta confirmada, disfruta la pelicula, recuerda que este boleto es gratis, pero debes estar 15 minutos antes de la funcion para realizar el registro correspondiente y la verificacion del requisito de la edad")
                else:
                    print ("Gracias por visitarnos, vuelva pronto")
                break

            elif edad >= 5 and edad <= 11:
                print ("El valor de la boleta es de $5000")
                confirmacion = input ("¿Deseas confirmar la compra de tu boleta: S/N: ").lower()
                if confirmacion == "s":
                    print ("Boleta confirmada, disfruta la pelicula. Valor a cancelar $5000, recuerde estar 15 minutos antes de la funcion para realizar el pago. Este se realizara con el documento de identidad correspondiente para la verificacion del requisito de la edad")
                else:
                    print ("Gracias por visitarnos, vuelva pronto")
                break

            elif edad >= 12 and edad <= 59:
                print ("El valor de la boleta es de $8000")
                confirmacion = input ("¿Deseas confirmar la compra de tu boleta?: S/N: ").lower()
                if confirmacion == "s":
                    print ("Boleta confirmada, disfruta la pelicula, valor a cancelar $8000, recuerde estar 15 minutos antes de la funcion para realizar el pago. Este se realizara con el documento de identidad correspondiente para la verificacion del requisito de la edad")
                else:
                    print ("Gracias por visitarnos, vuelva pronto")
                break

            elif edad >= 60:
                print ("El valor de la boleta es de $4000")
                confirmacion = input ("¿Deseas confirmar la compra de tu boleta?: S/N: ").lower()
                if confirmacion == "s":
                    print ("Boleta confirmada, disfruta la pelicula, valor a cancelar $4000, recuerde estar 15 minutos antes de la funcion para realizar el pago. Este se realizara con el documento de identidad correspondiente para la verificacion del requisito de la edad")
                else:
                    print ("Gracias por visitarnos, vuelva pronto")
                break

        elif cuantos_boletos == "varios":
            advertencia = input ("Recuerde que para la compra de varios boletos, el grupo de personas debe estar dentro del mismo rango de edad; estos son: (niños de 4 años o menores, entre 5 y 11 años, de 12 a 59 años y de 60 años en adelante. ¿Las personas del grupo tienen el mismo rango de edad?) S/N: ").lower()
            if advertencia == "s":
                numero_boletos = int(input ("¿Cuantos boletos deseas comprar?: "))
                edad_grupo = int(input ("Por favor ingresa una de las edades: "))
                if edad_grupo < 0:
                    print ("Edad invalida, por favor ingresa una edad correcta")
            
            if edad_grupo < 5:
                        valor_total = numero_boletos * 0
                        confirmacion = input ("El valor total a pagar por", numero_boletos, "boletas es de: $", valor_total, ",desea confirmar la compra de las boletas gratis?: S/N: ").lower()
                        if confirmacion == "s":
                            print ("Boletas confirmadas, disfruten la pelicula, recuerden que estos boletos son gratis, pero deben estar 15 minutos antes de la funcion para realizar el registro correspondiente y la verificacion del requisito de la edad")
                        else:
                            print ("Gracias por visitarnos, vuelva pronto")

            elif edad_grupo >= 5 and edad_grupo <= 11:
                        valor_total = numero_boletos * 5000
                        confirmacion = input("El valor total a pagar por", numero_boletos, "boletas es de: $", valor_total, ", desea confirmar la compra de las boletas?: S/N: ").lower()
                        if confirmacion == "s":
                            print ("Boletas confirmadas, disfruten la pelicula. Valor a cancelar $", valor_total, ", recuerden estar 15 minutos antes de la funcion para realizar el pago. Este se realizara con el documento de identidad correspondiente para la verificacion del requisito de la edad")
                        else:
                            print ("Gracias por visitarnos, vuelva pronto")

            elif edad_grupo >= 12 and edad_grupo <= 59:
                        valor_total = numero_boletos * 8000
                        confirmacion = input ("El valor total a pagar por", numero_boletos, "boletas es de: $", valor_total, ", desea confirmar la compra de las boletas?: S/N: ").lower()
                        if confirmacion == "s":
                            print ("Boletas confirmadas, disfruten la pelicula, valor a cancelar $", valor_total, ", recuerden estar 15 minutos antes de la funcion para realizar el pago. Este se realizara con el documento de identidad correspondiente para la verificacion del requisito de la edad")
                        else:
                            print ("Gracias por visitarnos, vuelva pronto")

            elif edad_grupo >= 60:
                        valor_total = numero_boletos * 4000
                        confirmacion = input ("El valor total a pagar por", numero_boletos, "boletas es de: $", valor_total, ", desea confirmar la compra de las boletas?: S/N: ").lower()  
                        if confirmacion == "s":
                            print ("Boletas confirmadas, disfruten la pelicula, valor a cancelar $", valor_total, ", recuerden estar 15 minutos antes de la funcion para realizar el pago. Este se realizara con el documento de identidad correspondiente para la verificacion del requisito de la edad")
                        else:
                            print ("Gracias por visitarnos, vuelva pronto")                         
                
        else:
                print ("Opcion invalida, por favor ingresa una opcion correcta")
                continue
            
            