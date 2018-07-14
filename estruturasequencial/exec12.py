#!/usr/bin/python3
#mostra o peso ideal de uma pessoa com base na altura digitada

altura = float(input('Digite a sua altura: '))

pesoideal = (72.7*altura) - 58

print('Sua altura é {} e seu peso ideal deve ser {} kg!'.format(altura, pesoideal))