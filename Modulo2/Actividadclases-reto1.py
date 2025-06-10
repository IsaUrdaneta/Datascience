#Gestor de Números Pares e Impares

#creando lista de números
numeros = []

#Desplegar el menú de opciones
opcion = ''
while opcion != "4":
    print("1. Ver lista completa")
    print("2. Ver sólo los números pares")
    print("3. Ver sólo los números impares")
    print("4. Salir del programa")
    opcion = input("Seleccione una opción: ")

    #Evaluando diferentes opciones
    if opcion == "1":
        numero = int(input('Ingrese número: '))
        numeros.append(numero)
        print("Lista completa de números:", numeros)

    elif opcion == "2":
        pares = []
        for n in numeros:
            if n % 2 == 0:
                pares.append(n)
        print("Números pares:", pares)

    elif opcion == "3":
        impares = []
        for n in numeros:
            if n % 2 != 0:
                impares.append(n)
        print("Números impares:", impares)

    elif opcion == "4":
            print("Saliendo del programa...")
    
    else:
        print('Opción inválida')
   




