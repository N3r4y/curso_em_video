# Desafio 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal


num = int(input('Insira um número inteiro: '))
print('Qual base de conversão você deseja usar?:'
      '\n\033[33m1\033[m - Binário'
      '\n\033[33m2\033[m - Octal'
      '\n\033[33m3\033[m - Hexadecimal')
esc = int(input('Insira uma opção: '))

if esc == 1:
    print('{} Convertido para binário é igual à {} em binário'.format(num, bin(num)[2:]))
elif esc == 2:
    print('{} Convertido para binário é igual à {} em octal.'.format(num, oct(num)[2:]))
elif esc == 3:
    print('{} Convertido para binário é igual à {} em hexadecimal.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
