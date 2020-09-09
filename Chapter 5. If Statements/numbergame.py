pienso = 2356
numero = int(input('Introduce un numbero entero: '))

while numero != pienso:
    if numero < pienso:
        print('\nEstas por debajo Iemi, intentalo de nuevo!')
        numero = int(input('Introduce otro numero: '))
    else:
        print('\nEstas por encima cangrejito, intentalo de nuevo!')
        numero = int(input('Introduce otro numero: '))

print(f'\nEnhorabuena pequitas, estaba pensando en el numero {pienso}!')


