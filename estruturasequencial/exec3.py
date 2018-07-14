#!/usr/bin/python3
#Pede dois números e mostra a soma dos mesmos

soma = 0
for x in range(2):
    num = int(input('Digite o número {}: '.format(x+1)))
    soma += num

print(soma)