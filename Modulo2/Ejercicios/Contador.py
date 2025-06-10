#Contador de Palabras

#solicitar ingresar datos
frase = input("Ingrese una frase: ")

#modulo split
palabras = frase.split()
cuentapalabras = len(palabras)

#resultado
print(palabras)
print(f"El número de palabras es: {cuentapalabras}")

