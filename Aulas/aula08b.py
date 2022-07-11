import random
from math import sqrt

num = random.randint(1, 1000)

print('Número selecionado: ', num)
print('A raiz quadrada de {} é {:.2f}!'.format(num, sqrt(num)))


