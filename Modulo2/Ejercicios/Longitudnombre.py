#Longitud de nombre

#solicitar ingresar datos
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")

#modulo split
nombrecompleto = nombre + apellido
longitud = len(nombrecompleto)

#resultado
print(f"La longitud del nombre es: {longitud}")