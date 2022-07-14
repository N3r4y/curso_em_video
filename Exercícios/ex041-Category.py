# Desafio 041 - A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre a sua categoria, de acordo com a idade.
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 Anos: Sênior
# Acima: Master

from datetime import date

nasc = int(input('Insira o ano de nascimento do atleta: '))

idade = date.today().year - nasc

if idade <= 9:
    print('O atleta tem {} anos. Sua categoria é Mirim!'.format(idade))
elif (idade > 9) and (idade <= 14):
    print('O atleta tem {} anos. Sua categoria é Infantil!'.format(idade))
elif (idade > 14) and (idade <= 19):
    print('O atleta tem {} anos. Sua categoria é Junior!'.format(idade))
elif (idade > 19) and (idade <= 20):
    print('O atleta tem {} anos. Sua categoria é Sênior!'.format(idade))
else:
    print('O atleta tem {} anos. Sua categoria é Master!'.format(idade))
