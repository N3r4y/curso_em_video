# Desafio 015 - Escreve um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por
# Km rodado.

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
print('O total a pagar é de R${:.2f}.'.format((d*60)+(km*0.15)))
