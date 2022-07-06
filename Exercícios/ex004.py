# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

n = input('Digite algo: ')
print('     O valor digitado é do tipo', type(n))
print('\nO valor digitado é:\n')
print('Numérico?', n.isnumeric())
print('Identificador?', n.isidentifier())
print('Alfanumérico?', n.isalnum())
print('Alfabético?', n.isalpha())
print('ASCII?', n.isascii())
print('Decimal?', n.isdecimal())
