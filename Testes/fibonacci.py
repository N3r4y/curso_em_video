# Considere a função fibo(), a seguir, cujo objetivo seria retornar o 'n-ésimo' elemento da Série de Fibonacci

n = 4


def fibo(n):
    fib = 0
    ant1 = 0
    ant2 = 1
    for i in range(0, n, 1):
        fib = ant1 + ant2
        ant1 = ant2
        ant2 = fib
    return fib


print(fibo(n))

#0 1 1 2 3 5
