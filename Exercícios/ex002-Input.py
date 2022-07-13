# Desafio 002 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'verde':'\033[4:32m'}

nome = input('Qual é o seu nome? ')
print('É muito bom te conhecer, {}{}{}!'.format(cores['verde'], nome, cores['limpa']))
