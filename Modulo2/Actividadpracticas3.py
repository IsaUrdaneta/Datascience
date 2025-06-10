#Desarrollar un programa en Python para evaluar las calificaciones y determinar 
#si cada estudiante ha aprobado o necesita mejorar en alguna asignatura

#while

#Desplegar el menú de opciones
opcion = ''
while opcion != "2":
    print("1. Ingresar datos de estudiante")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    #Evaluando diferentes opciones
    if opcion == "1":
        
        #creando lista de nombres
        nombres = []

        #Ingrese el nombre y la calificación de un estudiante
        nombre = input('Ingrese nombre del estudiante: ')
        
        #ingresando calificaciones
        
        #Lista de calificaciones
        list = []
        
        #primera materia
        calificacion1 = int(input('Ingrese calificación del estudiante en Matemáticas: '))
        #Evalúa si la calificación es aprobatoria
        if calificacion1 >= 60:
            print('Aprobado')
        else:
            print('Reprobado')
        
        #segunda materia
        calificacion2 = int(input('Ingrese calificación del estudiante en Ciencias: '))
        #Evalúa si la calificación es aprobatoria
        if calificacion2 >= 60:
            print('Aprobado')
        else:
            print('Reprobado')
        
        #tercera materia
        calificacion3 = int(input('Ingrese calificación del estudiante en Ciencias: '))
        #Evalúa si la calificación es aprobatoria
        if calificacion3 >= 60:
            print('Aprobado')
        else:
            print('Reprobado')
        
        #generando lista de calificaciones
        list = [calificacion1, calificacion2, calificacion3]

        #calculando el promedio de las calificaciones
        promedio = sum(list)//len(list)

        print(f'El promedio de notas es: {promedio}')

        #comentando el promedio
        comentarios =[]

        if promedio >= 90:
            comentario = 'El promedio es excelente'
        elif promedio < 90 and promedio >= 75:
            comentario = 'El promedio es bueno'
        elif promedio < 75:
            comentario ='El promedio es bajo, necesita mejorar'
        elif promedio < 0 or promedio > 100:
            comentario ='Ingrese calificaciones válidas'
        
        print(comentario)

        #guardar en listas
        nombres.append(nombre)
        comentarios.append(comentario)

    #imprimir resultados
    print('Resumen de calificaciones')
        
    for i in range(len(nombres)):
        print(f"{nombres[i]}: {comentarios[i]}")

    #mensaje usando expresión ternaria