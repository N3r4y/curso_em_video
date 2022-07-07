# Desafio 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número inteiro: '))
print('O antecessor do número {} é {} e o seu sucessor é {}.'.format(num, (num-1), (num+1)))