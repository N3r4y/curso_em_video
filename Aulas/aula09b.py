# Prática

frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print('''Após um intervalo de duas semanas, a Copa do Brasil volta a prender 
às atenções do torcedor a partir desta terça-feira, quando começam as partidas 
de volta das oitavas de final da competição. Que vem sendo chamada por muitos 
como "a maior da história".''')

print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase[0])

print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))

print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])