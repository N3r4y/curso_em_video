# Desafio 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

from random import randint

vel = randint(40, 150)

print('Sua velocidade foi de: {}Km/h'.format(vel))
if vel >= 80:
    velex = float(vel - 80)
    print('\033[31mVocê excedeu a velocidade limite em {:.0f}Km/h e foi multado no valor de R${:.2f}.\033[m'.format(velex, velex*7))
    print('\nDiriga com segurança!')
else:
    print('\033[33mVocê não foi multado!\033[m')
    print('\033[33mParabéns! Você é um ótimo cidadão!\033[m')
