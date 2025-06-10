#listas
number = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
total = 0

for i in number:
    total += i
print(total)


#ejercicio2
number2 = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
unique_number2 = []

for i in number2:
    if i not in unique_number2:
        unique_number2.append(i)

print('Los números únicos son: ', unique_number2)


#ejercicio3
suma = sum(number2)
suma_unicos = sum(unique_number2)
print('La suma de los números es: ', suma)