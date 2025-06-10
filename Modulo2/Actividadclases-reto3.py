#Panel de Control de Estudiantes

#Datos
estudiantes = {'Juan': 70, 'Marco': 90, 'José': 100}

#Desplegar el menú de opciones
opcion = ''
while opcion != "5":
    print("1. Ver todos los estudiantes")
    print("2. Agregar nuevo estudiante")
    print("3. Mostrar estudiantes aprobados y reprobados")
    print("4. Calcular el promedio general")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    #Evaluando diferentes opciones
    if opcion == "1":
        print('Lista de estudiantes: ')

        for nombre, nota in estudiantes.items():
            #incluyendo expresión ternaria
            comentario = " ¡Puntuación perfecta!" if nota == 100 else ""
            print(f"{nombre}: {nota}{comentario}")


    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante: ")
        nota_str = int(input("Ingrese la calificación: "))
        estudiantes[nombre] = nota
        print(f"{nombre} agregado con nota {nota}.")
     
    elif opcion == "3":
        print("\nAprobados (>= 60):")
        for nombre, nota in estudiantes.items():
            if nota >= 60:
                #incluyendo expresión ternaria
                comentario = " ¡Puntuación perfecta!" if nota == 100 else ""
                print(f"{nombre}: {nota}{comentario}")

        print("\nReprobados (< 60):")
        for nombre, nota in estudiantes.items():
            if nota < 60:
                print(f"{nombre}: {nota}")

    elif opcion == "4":
        if estudiantes:
            promedio = sum(estudiantes.values()) / len(estudiantes)
            print(f"Promedio general: {promedio}")
        else:
            print("No hay estudiantes registrados")

    elif opcion == "5":
        print("Saliendo del programa")

    else:
        print("Opción inválida. Intente de nuevo")

    
