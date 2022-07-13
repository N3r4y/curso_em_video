# Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

sal = float(input('Digite o seu salário: R$'))
aum = float(input('Digite o percentual de aumento: '))
print('\nO seu novo salário, agora com 15% de aumento é R${:.2f}'''.format(sal+(sal*aum/100)))
