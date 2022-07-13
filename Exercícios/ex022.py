# Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e motre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras tem ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

# Fernando Rafael Fernandes Nery

nome = str(input('Insira o seu nome completo: ')).strip()

print('Analisando seu nome...\n')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))