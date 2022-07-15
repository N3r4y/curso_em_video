# Desafio 045 - Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print('='*41)
print('Rock - Paper - Scissors - Lizard - Spock')
print('='*41)
print('Make your move!')
print('\033[33m1\033[m - Rock'
      '\n\033[33m2\033[m - Paper'
      '\n\033[33m3\033[m - Scissors'
      '\n\033[33m4\033[m - Lizard'
      '\n\033[33m5\033[m - Spock')

joken = {'1': 'Rock',
         '2': 'Paper',
         '3': 'Scissors',
         '4': 'Lizard',
         '5': 'Spock'}

esc = int(input('What is your choice? '))

print('Jo...')
sleep(1)
print('Ken...')
sleep(1)
print('Po...')
sleep(1)

opcs = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
escpc = random.choice(opcs)

if escpc == 'Rock' and esc == 2:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[32mPaper covers rock!\033[m \033[32mYou win!\033[m'.format(escpc, joken['2']))
elif escpc == 'Rock' and esc == 3:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[31mRock crushes scissors!\033[m \033[31mYou lose!\033[m'.format(escpc, joken['3']))
elif escpc == 'Rock' and esc == 4:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[31mRock crushes lizard!\033[m \033[31mYou lose!\033[m'.format(escpc, joken['4']))
elif escpc == 'Rock' and esc == 5:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[32mSpock vaporizes Rock!\033[m \033[32mYou win!\033[m'.format(escpc, joken['5']))

elif escpc == 'Paper' and esc == 1:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[31mPaper covers rock!\033[m \033[31mYou lose!\033[m'.format(escpc, joken['1']))
elif escpc == 'Paper' and esc == 3:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[32mScissors cuts paper!\033[m \033[32mYou win!\033[m'.format(escpc, joken['3']))
elif escpc == 'Paper' and esc == 4:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[32mLizard eats paper!\033[m \033[32mYou win!\033[m'.format(escpc, joken['4']))
elif escpc == 'Paper' and esc == 5:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[31mPaper disproves Spock!\033[m \033[31mYou lose!\033[m'.format(escpc, joken['5']))

elif escpc == 'Scissors' and esc == 1:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[32mRock crushes scissors!\033[m \033[32mYou win!\033[m'.format(escpc, joken['1']))
elif escpc == 'Scissors' and esc == 2:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[31mScissors cuts paper!\033[m \033[31mYou lose!\033[m'.format(escpc, joken['2']))
elif escpc == 'Scissors' and esc == 4:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[31mScissors decapitates lizard!\033[m \033[31mYou lose!\033[m'.format(escpc, joken['4']))
elif escpc == 'Scissors' and esc == 5:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[32mSpock smashes scissors!\033[m \033[32mYou win!\033[m'.format(escpc, joken['5']))

elif escpc == 'Lizard' and esc == 1:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[32mRock crushes lizard!\033[m \033[32mYou win!\033[m'.format(escpc, joken['1']))
elif escpc == 'Lizard' and esc == 2:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[31mLizard eats paper!\033[m \033[31mYou lose!\033[m'.format(escpc, joken['2']))
elif escpc == 'Lizard' and esc == 3:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[32mScissors decapitates lizard!\033[m \033[32mYou win!\033[m'.format(escpc, joken['3']))
elif escpc == 'Lizard' and esc == 5:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[31mLizard poisons Spock!\033[m \033[31mYou lose!\033[m'.format(escpc, joken['5']))

elif escpc == 'Spock' and esc == 1:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[31mSpock vaporizes rock!\033[m \033[31mYou lose!\033[m'.format(escpc, joken['1']))
elif escpc == 'Spock' and esc == 2:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[32mPaper disproves Spock!\033[m \033[32mYou win!\033[m'.format(escpc, joken['2']))
elif escpc == 'Spock' and esc == 3:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[31mSpock smashes scissors!\033[m \033[31mYou lose!\033[m'.format(escpc, joken['3']))
elif escpc == 'Spock' and esc == 4:
    print('\nI picked \033[32m{}\033[m. '
          '\nYou picked \033[32m{}\033[m. '
          '\n\033[32mLizard poisons Spock!\033[m \033[32mYou win!\033[m'.format(escpc, joken['4']))

else:
    print('\nWe both chose {}.'.format(escpc))
    print('\033[33mIt is a draw!\033[m')
