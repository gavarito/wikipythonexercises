#!/usr/bin/python3
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
#pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
#de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

from math import ceil

auton_lata = 54
area = float(input('Digite o tamanho em metros quadrados da area a ser pintada: '))

qtd_latas = area / auton_lata
preco = qtd_latas * 80

print('- Quantidade de latas a comprar: {:.2f}.\n Valor a pagar: R$ {:.2f}'.format(ceil(qtd_latas), preco))