# Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# km hm dam m dm cm mm

v = float(input('Ensira um valor em metros: '))
print('{}m tem: \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm!'.format(v, v/1000, v/100, v/10, v*10, v*100, v*1000))
