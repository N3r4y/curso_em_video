# Desafio 011 - Faça um programa que leia a largura e a algura de uma parede em metros, calcula a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

lar = float(input('Qual é a largura da parede? '))
alt = float(input('Qual é a altura da parede? '))

print('Para pintar a área total de {:.0f}m² serão necessários {:.1f} litros de tinta.'.format(lar*alt, (lar*alt)/2))
