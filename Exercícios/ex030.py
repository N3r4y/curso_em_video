# Desafio 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número inteiro: '))

if (num % 2) == 0:
    print("{0} é par!".format(num))
else:
    print("{0} é ímpar!".format(num))
