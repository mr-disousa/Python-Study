# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$ 0,15 por km rodado.

dias = int(input('Quantos dias de aluguel? '))
km = float(input('Qual o km percorrido? '))
pd = float(dias * 60.00)
kmp = float(km * 0.15)
vt = kmp + pd
print('O total do aluguel é de R${:.2f}'.format(vt))



