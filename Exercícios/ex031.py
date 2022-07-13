# Desafio 031 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcula o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

dist = int(input('Qual é a distância da sua viagem? '))

if dist <= 200:
    val = dist*0.5
    # print('O valor da viagem é R${:.2f}'.format(val))
else:
    val = dist*0.45
    # print('O valor da viagem é R${:.2f}'.format(val))
print('O preço de sua passagem será de R${:.2f}'.format(val))
# print('\nTenha uma boa viagem!')
