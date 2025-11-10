edad = int (input ("Ingrese su edad: "))
if edad < 0:    
            print ("Edad invalida, por favor ingresa una edad correcta")
        
elif edad >= 0 and edad < 5:
                print ("El valor de la boleta es gratis")
elif edad >= 5 and edad <= 11:
                print ("El valor de la boleta es de $5000")
elif edad >= 12 and edad <= 59:
                print ("El valor de la boleta es de $8000")
elif edad >= 60:
             print ("El valor de la boleta es de $4000")