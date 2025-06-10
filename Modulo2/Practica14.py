#Crea un programa en python que pida al usuario su edad y luego muestre una calificación según el rango de edad ingresado

edad = int(input("Ingrese una edad: "))

if edad <= 0 or edad > 120:
    print("Edad invalida")
elif edad > 0 and edad < 12:
    print("Niño")
elif edad > 13 and edad < 17:
    print("Adolescente")
elif edad > 18 and edad < 59:
    print("Adulto")
elif edad > 59 and edad < 120:
    print("Adulto Mayor")