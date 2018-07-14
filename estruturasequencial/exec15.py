#!/usr/bin/python3
# Calcula o salario liquido descontando IR, INSS, Sindicato.

val_hora = float(input('Digite o valor por hora: '))
horas_trab = int(input('Digite a quantidade de horas trabalhadas no mês: '))
sal_brut = val_hora * horas_trab
ir = sal_brut * 0.11
inss = sal_brut * 0.08
sind = sal_brut * 0.05
total_desc = ir + inss + sind
sal_liq = sal_brut - total_desc

print('+ Salário Bruto : R$ {}'.format(sal_brut))
print('- IR (11%) : R$ {:.2f}'.format(ir))
print('- INSS (8%) : R$ {}'.format(inss))
print('- Sindicato (5%) : R$ {}'.format(sind))
print('= Salário liquido : R$ {:.2f6}'.format(sal_liq))
