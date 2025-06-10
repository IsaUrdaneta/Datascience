#Escribe un programa en Python que recorra cada letra
# de una palabra utilizando un ciclo while.
# El programa debe imprimir la posición de cada letra
# y la letra correspondiente.
# Por ejemplo, si la palabra es "gato", el programa debe mostrar

# Letra en posición 0: g  
# Letra en posición 1: a  
# Letra en posición 2: t  
# Letra en posición 3: o

palabra = input("Ingrese una palabra: ")
indice = 0

#while
while indice < len(palabra):
    print("Letra en posicion {}: {}".format(indice,palabra[indice]))
    indice +=1