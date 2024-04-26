#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#EX: Digite um numero : 6.127
#O numero 6.127 tem a parte inteira 6


import math
num = float(input('Digite um numero '))
ra = round(num)
print('O numero {} arredondado é {}'.format(num,ra))

#ou

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}' .format(num, trunc(num)))
