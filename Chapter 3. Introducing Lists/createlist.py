list = []
list.append(input('Introduce el primer nombre de la lista: '))
count = 0

# Agregamos valores a la lista.
while count < 5:
    list.append(input('Introduce el siguiente nombre: '))
    count += 1
print(list)
print(f'El ultimo registrado es: {list[-1]}.')

# Imprimimos los valores de la lista
for x in list:
    print(x)
print(len(list))




