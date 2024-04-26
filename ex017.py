# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule
# e mostre o comprimento da hipotenusa

import math
cat_op = float(input('Qual a medida do cateto oposto? '))
cat_adj= float(input('Qual a medida do cateto adjacente? '))

hi = (cat_adj ** 2 + cat_op **2)**(1/2)

print('O valor da hipotenusa é {:.2f}'.format(hi))


#ou

import math
co = float(input('comprimento do cateto oposto '))
ca = float(input('comprimento do cateto adjacente '))
hi = math.hypot(co, ca)
print(' A hipotenusa será {:.2f}' .format(hi))
