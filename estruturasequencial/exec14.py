#!/usr/bin/python3
#Calcula o peso excedente de um limite e calcula a multa com base no peso excedente.

peso = int(input('Digite a quantidade de quilos pescados: '))

if peso > 50:
    excesso = peso - 50
    multa = float(excesso * 4)
    print('Voce pescou {} kg excedendo {} kg do limite. A multa a pagar é de R$ {:.2f}.'.format(peso, excesso, multa))
else:
    print('Você não excedeu o limite!')


