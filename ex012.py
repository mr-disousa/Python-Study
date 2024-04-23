# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto


v = float(input('Qual o preço do produto'))
d = float(input('Qual o desconto'))
des = v*d/100
vf = v-des
print('O preço do seu produto é R${:.2}' .format(vf))
