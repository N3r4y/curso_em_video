# Desafio 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação
# mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Quál é o valor do imóvel? '))
sal = float(input('Qual é o salário do comprador? '))
temp = int(input('Em quantos anos deseja pagar? '))

valprest = valor / (temp * 12)

if valprest > sal*0.3:
    print('\033[31mFinanciamento reprovado! O valor da parcela excede 30% do salário!\033[m'
          '\nValor total do financiamento: R${:.2f}'
          '\nNúmero de parcelas: {}'
          '\nValor das parcelas: R${:.2f}'.format(valor, temp * 12, valprest))
else:
    print('\033[32mParabéns! Seu financiamento está pré-aprovado.\033[m'
          '\nValor total do financiamento: R${:.2f}'
          '\nNúmero de parcelas: {}'
          '\nValor das parcelas: R${:.2f}'.format(valor, temp * 12, valprest))
