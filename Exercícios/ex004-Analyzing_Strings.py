# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

n = input('Digite algo: ')

print('\nO valor digitado é do tipo'.format(n), type(n))
print('\n{} é um número?'.format(n), n.isnumeric())
print('{} é um identificador?'.format(n), n.isidentifier())
print('{} é alfanumérico?'.format(n), n.isalnum())
print('{} é alfabético?'.format(n), n.isalpha())
print('{} é ASCII?'.format(n), n.isascii())
print('{} é decimal?'.format(n), n.isdecimal())
print('{} só tem espaços?'.format(n), n.isspace())
print('{} está em maiúsculas?'.format(n), n.isupper())
print('{} está em minúsculas?'.format(n), n.islower())
print('{} está capitalizada?'.format(n), n.istitle())

print('{} é um valor decimal?'.format(n), n.isdecimal())
