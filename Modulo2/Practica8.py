#programa que valida si un numero es par

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#codigo equivalente
paridad = "par" if numero % 2 == 0 else "impar"
print(paridad)