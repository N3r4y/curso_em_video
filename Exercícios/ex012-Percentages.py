# Desafio 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Informe o preço do produto: R$'))
d = float(input('Informe o percentual de desconto: '))
print('O preço do produto com 5% de desconto é R${:.2f}.'.format(p-(p*d/100)))
