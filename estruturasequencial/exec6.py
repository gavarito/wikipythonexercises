#!/usr/bin/python3
#Pede o raio e calcula a área de um círculo

from math import pi

raio = float(input('Digite o raio do circulo: '))
area = (pi * (raio ** 2))

print('A área do círculo é {}.'.format(area))