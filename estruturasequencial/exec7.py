#!/usr/bin/python3
#Pede o tamanho dos lados e calcula a área de um quadrado

from math import pow

lado = int(input('Digite o tamanho dos lados do quadrado: '))
result = pow(lado, 2) * 2

print('O valor é {}'.format(result))