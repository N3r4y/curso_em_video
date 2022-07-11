# Desafio 017 -  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

'''catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjacente: '))
hypot = (catop ** 2 + catad ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hypot))'''

from math import hypot

catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjacente: '))

print('\nA hipotenusa de um triângulo retângulo onde:\n - o cateto oposto é {}\n - e o cateto adjacente é {}\n'
      'é {:.2f}'.format(catop, catad, hypot(catop, catad)))
