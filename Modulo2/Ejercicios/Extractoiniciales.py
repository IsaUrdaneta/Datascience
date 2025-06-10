#Extracto de Iniciales

#solicitar ingresar datos
nombre = input("Ingrese nombre completo: ")

#modulo split
iniciales = next(zip(*nombre.split()))

#resultado
print(f"Las iniciales son: {iniciales}")