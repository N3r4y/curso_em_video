# Desafio 045 - Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print('='*20)
print('JOKENPÔ')
print('='*20)
print('Faça a sua jogada')
print('\033[33m1\033[m - Pedra'
      '\n\033[33m2\033[m - Papel'
      '\n\033[33m3\033[m - Tesoura')

joken = {'1': 'Pedra',
         '2': 'Papel',
         '3': 'Tesoura'}

esc = int(input('Qual é a sua escolha? '))

opcs = ['Pedra', 'Papel', 'Tesoura']
escpc = random.choice(opcs)

if escpc == 'Pedra' and esc == 2:
    print('\nEu escolhi \033[32m{}\033[m. Você escolheu \033[32m{}\033[m.'.format(escpc, joken['2']))
    print('\033[32mVocê ganhou!\033[m')
elif escpc == 'Pedra' and esc == 3:
    print('\nEu escolhi \033[32m{}\033[m. Você escolheu \033[32m{}\033[m.'.format(escpc, joken['3']))
    print('\033[31mEu ganhei!\033[m')
elif escpc == 'Papel' and esc == 1:
    print('\nEu escolhi \033[32m{}\033[m. Você escolheu \033[32m{}\033[m.'.format(escpc, joken['1']))
    print('\033[31mEu ganhei!\033[m')
elif escpc == 'Papel' and esc == 3:
    print('\nEu escolhi \033[32m{}\033[m. Você escolheu \033[32m{}\033[m.'.format(escpc, joken['3']))
    print('\033[32mVocê ganhou!\033[m')
elif escpc == 'Tesoura' and esc == 1:
    print('\nEu escolhi \033[32m{}\033[m. Você escolheu \033[32m{}\033[m.'.format(escpc, joken['1']))
    print('\033[32mVocê ganhou!\033[m')
elif escpc == 'Tesoura' and esc == 2:
    print('\nEu escolhi \033[32m{}\033[m. Você escolheu \033[32m{}\033[m.'.format(escpc, joken['2']))
    print('\033[31mEu ganhei!\033[m')
else:
    print('\nNós dois escolhemos {}.'.format(escpc))
    print('\033[33mNós empatamos!\033[m')
