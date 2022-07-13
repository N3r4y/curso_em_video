# Desafio 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

cnum = randint(0, 5)

print('\033[33m-=-\033[m'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ')
print('\033[33m-=-\033[m'*20)

pnum = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)

if cnum == pnum:
    print('\n\033[32mVocê acertou! Eu pensei no número {}!\033[m'.format(cnum))
else:
    print('\n\033[31mVocê errou! Eu pensei no número {} e não no número {}!\033[m'.format(cnum, pnum))
