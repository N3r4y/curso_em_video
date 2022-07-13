frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '

print('\n')
print(frase)

# Fatiamento
print('\n\033[31mFatiamento\033[m')
print(frase[9])
print(frase[9:13])
print(frase[9:21:2])  #
print(frase[:5])  # Retorna a string contando até a quinta posição
print(frase[15:])  # Retorna a string contando a partir da décima quinta posição
print(frase[9::3])  # A partir da nona posição, retorna cada 3 posições até o final da string

# Análise
print('\n\033[31mAnálise\033[m')
print(len(frase))  # Conta o tamanho da string
print(frase.count('o'))  # Conta quantas vezes a letra 'o' existe na string
print(frase.find('deo'))  # Retorna o início da string procurada
print(frase.find('Android'))  # String não encontrada retorna -1
print('curso' in frase)

# Transformação
print('\n\033[31mTransformação\033[m')
print(frase.replace('Python', 'Android'))  # Substitiu a string Python pela string Android
print(frase.upper())  # Converte minúsculas para maiúsculas
print(frase.lower())  # Converte maiúsculas para minúsculas
print(frase.capitalize())  # Converte a primeira letra da frase para maiúscula
print(frase.title())  # Converte a primeira letra de casa palavra para maiúsculas
print(frase2.strip())  # Remove espaços inúteis
print(frase2.rstrip())  # Remove espaços inúteis à direita
print(frase2.lstrip())  # Remove espaços inúteis à esquerda

# Divisão
print('\n\033[31mDivisão\033[m')
print(frase.split())  # Divide os uma string em seus espaços em branco e separa as mesmas em listas distintas

# Junção
print('\n\033[31mJunção\033[m')
print('-'.join(frase))
