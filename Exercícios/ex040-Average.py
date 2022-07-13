# Desafio 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagen no final,
# de acordo com a média atingida

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

med = (n1 + n2) / 2

if med < 5.0:
    print('Reprovado! Sua média foi {:.1f}.'.format(med))
elif (med >= 5) and (med <= 6.9):
    print('Recuperação! Sua média foi {:.1f}.'.format(med))
else:
    print('Aprovado! Sua média foi {:.1f}.'.format(med))
