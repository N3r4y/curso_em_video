# Desafio 024 - Crie um programa que leia o nome de uma cidade e diga se ele começa ou não com o nome 'SANTO'.

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')

