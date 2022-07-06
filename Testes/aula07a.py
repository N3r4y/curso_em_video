# Operadores aritméticos

# +. Adição
# -. Subtração
# *. Multiplicação
# /. Divisão
# %. Resto da divisão (sobra da divisão inteira)
# **. Potencialização
# //. Divisão inteira (sem usar virgula)

#Exemplos

# 5+2 == 7
# 5-2 == 3
# 5*2 == 10
# 5/2 == 2.5
# 5**2 == 25
# 5//2 == 2
# 5%2 == 1

# Ordem de precedência

# 1. ()
# 2. **
# 3. * / // %
# 4. + -

# Exemplo

# n = 5+3*2
# n = 3*5+4**2
# n = 3*(5+4)**2
# print(n)

# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# print('A soma vale {}'.format(n1+n2))
print('A soma é {}.\nO produto é {}.\nA divisão é {:.2f}'.format(s, m, d), end=' ')
print('\nA divisão inteira é {}.\nA potência é {}'.format(di, e))
