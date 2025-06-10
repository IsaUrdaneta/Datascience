#Calculo de costo por letra

#ingresar datos
palabra = input("Ingrese una palabra: ")
costo = int(input("Ingrese costo por letra (CLP): "))

#contar letras

total_letras = int(len(palabra))

costototal = (total_letras) * costo

#resultado
print(f"El costo total de la palabra es: {costototal}")