print ("Bienvenidos a Noche estelar")
print ("Recuerda que para confirmar tu ingreso debes realziar el registro virtual, ten a la mano tu documento de identidad por que sera necesario, nos vemos esta noche")
documento = input ("Posee su documento de identidad? (si/no): ").lower()
edad = int (input ("Ingrese su edad: "))
if edad >= 18 and documento == "si":
    print ("Registro exitoso, bienvenido a nuestro club")
elif edad < 18 and documento == "si":
        print ("Entrada Denegada, lo sentimos, no cumple con la edad requerida para ingresar al club")
elif edad >= 18 and documento == "no":
        print ("Lo sentimos, no puede ingresar sin su documento de identidad")
elif edad < 18 and documento == "no":
        print ("entrada Denegada, lo sentimos, no cumple con la edad requerida para ingresar al club y ademas no posee su documento de identidad")  
print ("Gracias por usar nuestro sistema de registro virtual")  