#Crie um programa que leia quanto dinnheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#considere U$$1,00 = R$3,27

m = float(input('Digite o valor R$:'))
c = float(m/3.27)
print('voce conseguirá comprar U$${:.2f}' .format(c))


