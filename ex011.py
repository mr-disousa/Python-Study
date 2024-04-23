# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area
# e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m².

a = float(input('Qual a altura da parade?'))
l = float(input('Qual a largura da parede?'))
parede = float(a*l)
tinta = float(parede)/2

print('O tamanho da sua parede é {} e quantidade de tinta será {}' .format(parede, tinta))

