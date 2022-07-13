# Desafio 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alista.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Qual é o seu ano de nascimento? '))

dif = date.today().year - nasc

if dif > 18:
    dif = dif - 18
    print('Já se passaram {} anos da data do seu alistamento militar obrigatório!'.format(dif))
elif dif < 18:
    dif = 18 - dif
    print('Falta {} anos para o seu alistamento militar obrigatório!'.format(dif))
else:
    print('Você deve se alistar no serviço militar obrigatório este ano!')
