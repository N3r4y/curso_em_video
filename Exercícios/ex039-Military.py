# Desafio 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alista.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
nasc = int(input('Qual é o seu ano de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade > 18:
    dif = idade - 18
    print('Já se passaram {} anos da data do seu alistamento militar obrigatório!'.format(dif))
    ano = atual + dif
    print('Seu alistamento foi em {}.'.format(ano))
elif idade < 18:
    dif = 18 - idade
    print('Falta {} anos para o seu alistamento militar obrigatório!'.format(dif))
    ano = atual - dif
    print('Seu alistamento será em {}.'.format(ano))
else:
    print('Você deve se alistar no serviço militar obrigatório este ano!')
