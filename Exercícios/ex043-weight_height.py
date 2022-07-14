# Desafio 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
# de acordo com a tabela abaixo.
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# De 25 até 30: Sobrepeso
# De 30 até 40: Obesidade
# Acima de 40: Obesiade mórbida

from time import sleep
import math

print('='*20)
print(' \033[33mCalculadora de IMC\033[m')
print('='*20)

peso = float(input('Insira o peso em Kg: '))
alt = int(input('Insira a sua altura em cm: '))
print('Calculando seu IMC...\n')
sleep(2)


imc = peso / (math.pow((alt / 100), 2))

if imc <= 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso ideal.'.format(imc))
elif (imc > 18.5) and (imc <= 25):
    print('\033[32mSeu IMC é {:.2f} e você está no peso ideal.\033[m'.format(imc))
elif (imc > 25) and (imc <= 30):
    print('Seu IMC é {:.2f} e você está com sobrepeso.'.format(imc))
elif (imc > 30) and (imc <= 40):
    print('Seu IMC é {:.2f} e você está obeso.'.format(imc))
else:
    print('\033[31mSeu IMC é {:.2f} e você está em nível de obesidade mórbida.\033[m'.format(imc))
