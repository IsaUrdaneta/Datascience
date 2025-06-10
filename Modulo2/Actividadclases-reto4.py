# Sumador Inteligente con Control de Corte

listanum = []
suma_total = 0

# Menú interactivo
opcion = ''
while opcion != "5":
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Ingresar un número")
    print("2. Ver suma total")
    print("3. Ver números ingresados")
    print("4. Reiniciar suma y lista")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        num = float(input("Ingrese un número: "))
        if num < 0:
            print("Se ingresó un número negativo. Saliendo del programa automáticamente.")
            break
        listanum.append(num)
        suma_total += num
        print(f"Número {num} agregado.")

    elif opcion == "2":
        print(f"La suma total es: {suma_total}")

    elif opcion == "3":
        print("Números ingresados:")
        for n in listanum:
            print(f"- {n}")

    elif opcion == "4":
        listanum = []
        suma_total = 0
        print("Suma y lista reiniciadas.")

    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")

    else:
        print("Opción inválida.")