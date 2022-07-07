num = int(input('Valor: '))

print('='*13)
for i in range(1, 11):
    v = num * i
    print('{} x {:2} = {}'.format(num, i, v))
print('='*13)
