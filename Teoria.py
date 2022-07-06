# Aula sobre tipos primitivos

# Quatro tipos primitivos mais básicos
# int   - 7, -4, 0, 9875
# float - 4.5, 0.076, -15.223, 7.0
# bool  - True, False (sempre com a primeira letra maiúscula)
# str   - 'Olá', '7.5' (Sempre entre aspas. Por convenção, aspas simples)

# Sem declarar o tipo

# n1 = input('Digite um número: ')
# n2 = input('Digite mais um número: ')
# s = n1 + n2

# print('A soma vale', s)

# Delarando o tipo

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite mais um número: '))
# s = n1 + n2

# print('A soma vale', s)

# Print formatado

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2

print('A soma vale {}!'.format(s))
