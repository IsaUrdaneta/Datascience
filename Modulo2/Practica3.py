nombre = 'Ana'
edad = '25'
altura = 1.65
print (f"{nombre} tiene {edad} años y mide {altura} metros")

nombre = input("Ingrese su nombre: ") #ingresa nombre
edad = int(input("Ingrese su edad: ")) #ingresa edad
altura = float(input("Ingrese su altura en metros: ")) #ingresa altura y convierte en flotante

#convierte en flotante
peso = float(input("Ingrese su peso en kilogramos: "))
pesolibras = peso * 2.20462 #convierte en libras
print (f"{nombre} tiene {edad} años y mide {altura} metros y peso en {pesolibras} libras") #imprime los datos