# Escreva um programa que leia um valor convertido em centimetros e milimetros

m = float(input('Digite a metragem: '))
cm = float(m)*100
mm = float(cm)*1000
print('Esse valor em metros, convertido para centimetros é {}cm e em milimetros {}'.format(cm,mm))

# Escreva um programa que leia um valor em metrosconvertido para quilômetro, hectômetro, decâmetro, metro,decímetro.centímetro.milímetro

m = float(input('Digite a metragem: '))
km = m / 1000
hm = km * 1000
dam = hm * 1000
dm = dam *1000
cm = dm * 1000
mm = cm * 1000
print('Esse valor em metros, convertido para Km é {}  e em hm {} e em dam {} e em dm {} e em cm {} e em mm {}'.format(km,hm,dam,dm,cm,mm))

