# Desafio 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Informe o salário: R$'))

if sal <= 1250:
    aum = sal * 1.15
    print('O novo salário acrescido de 15% é de R${:.2f}.'.format(aum))
else:
    aum = sal * 1.1
    print('O novo salário acrescido de 10% é de R${:.2f}.'.format(aum))
