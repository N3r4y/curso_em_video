# Desafio 042 - Refaça o desafio 031 dos triângulos, acrescentando o recurso de mostar que tipo de triângulo
# será formado.
# Equilatero - Todos os lados iguais
# Isósceles - Dois lados iguais
# Escaleno - Todos os lados diferentes

r1 = int(input('Insira o valor da primeira reta: '))
r2 = int(input('Insira o valor da segunda reta: '))
r3 = int(input('Insira o valor da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        print('As medidas {}, {} e {} formam um triângulo equilátero!'.format(r1, r2, r3))
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('As medidas {}, {} e {} formam um triângulo isósceles!'.format(r1, r2, r3))
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('As medidas {}, {} e {} formam um triângulo escaleno!'.format(r1, r2, r3))
else:
    print('As medidas {}, {} e {} não formam um triângulo!'.format(r1, r2, r3))


