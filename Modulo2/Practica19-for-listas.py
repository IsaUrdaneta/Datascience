#Mini base de datos

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennumber = []

for i in number:
    if i % 2 == 0:
        evennumber.append(i)
print('Los números pares son: ', evennumber)

#como se usa el for en otros lenguajes
#for ([expresion-inicial]; [condicion]; [expresion-final])
 