# Desafio 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

# result = [int(a) for a in str(num)]

# print('O número {} tem: \nUnidades: {}\nDezenas: {}\nCentanas: {}\nMilhares: {}.'.format(num, result[3], result[2],
#                                                                                          result[1], result[0]))

# Convertando int para str (com falha)
# num = int(input('Insira um número intenro de 0 a 9999: '))
# n = str(num)
# print('Analisando o número {}'.format(num))
# print('O número {} tem: \nUnidades: {}\nDezenas: {}\nCentanas: {}\nMilhares: {}.'.format(num, n[3], n[2], n[1], n[0]))

num = int(input('Insira um número intenro de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número {} tem: \nUnidades: {}\nDezenas: {}\nCentanas: {}\nMilhares: {}'.format(num, u, d, c, m))