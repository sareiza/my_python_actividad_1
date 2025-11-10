tecnica = 0.7
logica = 0.3

print ("Bienvenido a tecno plus")
print ("Realizamos el cálculo de las Evaluaciones Compuestas")
nota1 = float(input ("Ingrese la nota de la evaluación técnica: "))
nota2 = float(input ("Ingrese la nota de la evaluación lógica: "))

final = float((nota1 * tecnica) + (nota2 * logica))
print (f"Su nota final es: {final}")
if final >= 3:
    print ("Usted esta aprobado")
elif final < 3 and final >= 2:
    print ("Se necesita realizar una revisión")
elif final < 2:
    print ("Usted esta reprobado")

    print ("Gracias por usar nuestro sistema")


