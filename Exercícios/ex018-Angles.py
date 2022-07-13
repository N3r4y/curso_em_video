# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse
# ângulo.

from math import radians, sin, cos, tan

'''ang = float(input('Insira o ângulo desejado: '))

print('\nO valor das funções trigonométricas de um ângulo de {} radianos são:\n'
      'Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}\n'.format(ang, math.sin(ang), math.cos(ang), math.tan(ang)))'''


ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

