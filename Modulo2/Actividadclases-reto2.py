#Inventario de Frutas con tupla base

# Tupla inicial con frutas
frutas = ("manzana", "pera", "naranja", "manzana", "plátano")

# Lista para actualizar el inventario (se crea a partir de la tupla)
inventario = list(frutas)

# Menú interactivo
opcion = ''
while opcion != "5":
    print("\n--- MENÚ DE INVENTARIO DE FRUTAS ---")
    print("1. Ver todas las frutas")
    print("2. Contar cuántas veces aparece una fruta")
    print("3. Agregar una fruta al inventario")
    print("4. Mostrar inventario actualizado")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nFrutas disponibles:")
        for fruta in frutas:
            print(f"- {fruta}")

    elif opcion == "2":
        fruta_buscar = input("Ingrese el nombre de la fruta a contar: ").lower()
        cantidad = inventario.count(fruta_buscar)
        print(f"La fruta '{fruta_buscar}' aparece {cantidad} vez/veces en el inventario.")

    elif opcion == "3":
        nueva_fruta = input("Ingrese el nombre de la nueva fruta a agregar: ").lower()
        inventario.append(nueva_fruta)
        print(f"'{nueva_fruta}' fue agregada al inventario.")

    elif opcion == "4":
        print("\nInventario actualizado:")
        for fruta in inventario:
            print(f"- {fruta}")

    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")

    else:
        print("Opción inválida. Por favor, intente de nuevo.")