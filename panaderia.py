precio_pan = 300
while True: 
    print ("Bienvenido a Santo Pan, la promocion del dia es: por la compra de 20 panes obtienes 10 porciento de descuento, mas de 50 panes obtienes el 20 porciento descuento")
    respuesta = input("Deseas realizar una compra?: S/N: ").lower()
    if respuesta == "s":
        cantidad_panes = int(input("Que cantidad de panes deseas comprar?: "))
        if cantidad_panes < 20:
            valor_a_pagar = cantidad_panes * precio_pan
            print ("El valor a pagar por", cantidad_panes, "es de: ", valor_a_pagar)
            break

        if cantidad_panes >= 20 and cantidad_panes < 50:
            valor_a_pagar = ((cantidad_panes*precio_pan)-((cantidad_panes*precio_pan)*0.10))
            print ("El valor a pagar por", cantidad_panes, "es de: ", valor_a_pagar)
            break

        if cantidad_panes >= 50:
            valor_a_pagar = ((cantidad_panes*precio_pan)-((cantidad_panes*precio_pan)*0.20))
            print ("El valor a pagar por", cantidad_panes, "es de: ", valor_a_pagar)
            break
            
    else:
        print ("Gracias por visitarnos, vuelva pronto")
        break


