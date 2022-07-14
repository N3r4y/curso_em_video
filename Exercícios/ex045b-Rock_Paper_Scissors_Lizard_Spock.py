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

opcs = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
escpc = random.choice(opcs)

if escpc == 'Rock' and esc == 2:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['2']))
    print('\033[32mYou win!\033[m')
elif escpc == 'Rock' and esc == 3:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['3']))
    print('\033[31mI won!\033[m')
elif escpc == 'Rock' and esc == 4:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['4']))
    print('\033[31mI won!\033[m')
elif escpc == 'Rock' and esc == 5:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['5']))
    print('\033[31mYou win!\033[m')

elif escpc == 'Paper' and esc == 1:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['1']))
    print('\033[31mI won!\033[m')
elif escpc == 'Paper' and esc == 3:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['3']))
    print('\033[32mYou win!\033[m')
elif escpc == 'Paper' and esc == 4:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['4']))
    print('\033[32mYou win!\033[m')
elif escpc == 'Paper' and esc == 5:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['5']))
    print('\033[31mI won!\033[m')

elif escpc == 'Scissors' and esc == 1:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['1']))
    print('\033[32mYou win!\033[m')
elif escpc == 'Scissors' and esc == 2:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['2']))
    print('\033[31mI won!\033[m')
elif escpc == 'Scissors' and esc == 4:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['4']))
    print('\033[31mI won!\033[m')
elif escpc == 'Scissors' and esc == 5:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['5']))
    print('\033[32mYou win!\033[m')

elif escpc == 'Lizard' and esc == 1:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['1']))
    print('\033[32mYou win!\033[m')
elif escpc == 'Lizard' and esc == 2:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['2']))
    print('\033[31mI won!\033[m')
elif escpc == 'Lizard' and esc == 3:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['3']))
    print('\033[32mYou win!\033[m')
elif escpc == 'Lizard' and esc == 5:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['5']))
    print('\033[31mI won!\033[m')

elif escpc == 'Spock' and esc == 1:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['1']))
    print('\033[31mI won!\033[m')
elif escpc == 'Spock' and esc == 2:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['2']))
    print('\033[32mYou win!\033[m')
elif escpc == 'Spock' and esc == 3:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['3']))
    print('\033[31mI won!\033[m')
elif escpc == 'Spock' and esc == 4:
    print('\nI picked \033[32m{}\033[m. You picked \033[32m{}\033[m.'.format(escpc, joken['4']))
    print('\033[32mYou win!\033[m')

else:
    print('\nNós dois escolhemos {}.'.format(escpc))
    print('\033[33mNós empatamos!\033[m')

