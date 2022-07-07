# Desafio 10 - Crie um programa que leia quanto diheiro uma pessoa tem na carteira e mostre quandos dólares ela
# pode comprar. # Considere US$1,00 = R$3,27

d = float(input('Digite quantos reais você tem na carteira: R$'))
print('R${:.2f} estão valendo US${:.2f}.'.format(d, d/3.27))
