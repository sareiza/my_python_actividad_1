mastreintau = 0.15
masdiezu = 0.05

print ("Bienvenido a  su supermercado Ahorro MAX, con descuentos y envío")
print ("Realice su pedido")
cantidad = int (input ("Ingrese la cantidad de productos que desea comprar: "))
total = int (cantidad * 2000)
if cantidad < 10:
    final = total
    print (f"El total a pagar es: {final + 5000} pesos")

if cantidad >= 10 and cantidad <= 29:
    final = total - (total * masdiezu)
    if final < 50000:
        print (f"El total a pagar es: {final + 5000} pesos")
        

elif cantidad >= 30:
    final = total - (total * mastreintau)
    print (f"El total a pagar con descuento es: {final} pesos")

print ("Gracias por su compra, vuelva pronto")


