#!/usr/bin/python3
#Pede a temperatura em Farenheit e converte para Celsius

f = float(input('Digite a temperatura Farenheit: '))
c = (f-32) / 1.8

print('A temperatura em Celsius é: {}'.format(c))