# Desafio 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Informe o preço do produto: '))
print('O valor do produto com 5% de desconto fica R${:.2f}.'.format(p*0.95))
