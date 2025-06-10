#Mini base de datos

#Listas de letras 

letters = ['a', 'b', 'c', 'd', 'e']
reversed_letters = []

for i in range(len(letters)-1, -1, -1):
    reversed_letters.append(letters[i])
print(reversed_letters)


#range
range_number2 = range(11, 1, -1)
for i in range_number2:
    print(i)
print(type(range_number2))