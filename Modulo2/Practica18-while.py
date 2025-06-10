# Desarrolla un programa en Python que permita al usuario ingresar  4 números
#realizar operaciones aritméticas con ellos.
# Usa un menú interactivo con las siguientes opciones:
 
# Calcular y mostrar la suma total de los números ingresados.
 
# Calcular y mostrar el promedio de los números.
 
# Mostrar el número mayor y menor de la lista.
 
# Salir del programa.
 
# El menú debe repetirse usando un ciclo while
# hasta que el usuario elija salir.
# Asegúrate de validar las entradas numéricas

#menu
opcion = ""
while opcion != "4":
    print("1. Suma total de los números ingresados")
    print("2. Promedio de los números")
    print("3. Número mayor y menor de la lista")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    #Suma total de los números ingresados
    if opcion == "1":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))
        numero4 = float(input("Ingrese el cuarto número: "))
        resultado = numero1 + numero2 + numero3 + numero4
        print(f"La suma de los números ingresados es: {resultado}")
    
    #Promedio de los números
    elif opcion == "2":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))
        numero4 = float(input("Ingrese el cuarto número: "))
        resultado = (numero1 + numero2 + numero3 + numero4) // 4
        print(f"El promedio de los números ingresados es: {resultado}")
    
    #Número mayor y menor de la lista
    elif opcion == "3":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))
        numero4 = float(input("Ingrese el cuarto número: "))

        list = [numero1, numero2, numero3, numero4]
        
        print(f"El número mayor es: {max(list)} y el número menor es: {min(list)}")


    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opción no válida, por favor intente de nuevo.")

