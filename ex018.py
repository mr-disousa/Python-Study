# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste angulo.

import math

ang = float(input('Digite o angulo '))
rad = math.radians(ang)

seno = math.sin(rad)
coss = math.cos(rad)
tang = math.tan(rad)

print('O valor do seno é {:.2f}, já o valor de cosseno é {:.2f} e a tangente é {:.2f}'.format(seno, coss, tang))

#ou



