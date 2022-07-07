# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Informe a temperatura em ºC: '))
print('A temperatura de {}ºC corresponde a {}ºF!'.format(temp, (temp*9/5)+32))

# (0 °C × 9/5) + 32 = 32 °F
