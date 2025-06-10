#Genenador de contraseñas

#solicitar ingresar datos
nombre = input("Ingrese nombre: ")
numero = input("Ingrese numero: ")

#generar contraseña
contrasena = nombre + numero + "!"


#resultado
print(f"La contraseña es: {contrasena}")
