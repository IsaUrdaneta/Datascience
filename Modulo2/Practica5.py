#ingresar datos
capitalinicial = int(input("Ingrese capital inicial (USD): "))
tasadeinteres = float(input("Ingrese tasa de interés (%): "))
numerodeanos = int(input("Ingrese numero de años: "))

#calculo de interes simple
interessimple = (capitalinicial * tasadeinteres * numerodeanos) // 100

#mostrar el resultado
print(f"El interés simple es {interessimple}")