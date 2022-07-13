'''tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('---FIM---')


print('carro novo' if tempo <= 3 else 'carro velho')
print('---FIM---')

nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
# print('Parabéns!' if m >= 6 else 'Estude mais!')
if m >= 6.0:
    print('Sua média foi boa. Parabéns!')
else:
    print('Sua média foi ruim. Estude mais!')