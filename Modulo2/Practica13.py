# #asignar letra según clasificación
calificacion = int(input("Ingrese su calificacion: "))

if calificacion > 100 or calificacion < 0:
    print("Calificacion invalida")
elif calificacion >= 90 and calificacion <= 100:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("F")

