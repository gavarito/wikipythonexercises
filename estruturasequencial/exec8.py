#!/usr/bin/python3
#Pede o valor por hora e dias trabalhados e calcula o salário

hora = float(input('Digite o valor da hora trabalhada: '))
horas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario = hora * horas

print('Seu salário no referido mês foi R$ {}'.format(salario))