# Desafio 044 - Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# Em 3x ou mais no cartão: 20% de juros

val = float(input('Insira o valor do produto: R$'))

opcoes = {'1': 'à vista em dinheiro ou cheque',
          '2': 'à vista no cartão de crédito',
          '3': 'em 2x no cartão de crédito',
          '4': 'em 3x ou mais no cartão'}

print('\nOpções de pagamento: '
      '\n1 - À vista em dinheiro ou cheque'
      '\n2 - À vista no cartão de crédito'
      '\n3 - Em 2x no cartão de crédito'
      '\n4 - 3x ou mais no cartão')

opc = int(input('\nEscolha uma opção de pagamento: '))

if opc == 1:
    print('\nA opção escolhida foi {}.\nO valor total a pagar é de R${:.2f}.'.format(opcoes['1'],
                                                                                    val - ((val * 10) / 100)))
elif opc == 2:
    print('\nA opção escolhida foi {}.\nO valor total a pagar é de R${:.2f}.'.format(opcoes['1'],
                                                                                    val - ((val * 5) / 100)))
elif opc == 3:
    print('\nA opção escolhida foi {}.\nO valor total a pagar é de R${:.2f}.'.format(opcoes['1'],
                                                                                    val))
else:
    print('\nA opção escolhida foi {}.\nO valor total a pagar é de R${:.2f}.'.format(opcoes['1'],
                                                                                    val + ((val * 20) / 100)))
