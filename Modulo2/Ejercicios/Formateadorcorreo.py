#Formateador de Correo Electrónico

#solicitar ingresar datos

nombre = input("Ingrese nombre: ")
dominio = input("Ingrese dominio: ")

#concatenar
correo = nombre.lower() + "@" + dominio

#resultado
print(f"El correo electrónico es: {correo}")