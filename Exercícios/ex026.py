# Desafio 026 - Faça um prgorama que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra 'A'
# 2. Em que posição ela aparece a primeira vez
# 3. Em que posição ela aparece a última vez

# Atirei o pau no gato
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
