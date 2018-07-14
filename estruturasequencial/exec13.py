#!/usr/bin/python3
#Com base na altura e no sexo, calcula o peso ideal para a pessoa.

sexo = input('Digite seu sexo, M ou F: ')

if sexo.upper() == 'M':
    altura = float(input('Digite sua altura: '))
    pesoideal = (72.7*altura) - 58
    print('Sua altura é {}m e seu peso ideal deve ser {}kg.'.format(altura, pesoideal))
elif sexo.upper() == 'F':
    altura = float(input('Digite sua altura: '))
    pesoideal = (62.1*altura) - 44.7
    print('Sua altura é {}m e seu peso ideal deve ser {}kg.'.format(altura, pesoideal))
else:
    print('Opção incorreta!')