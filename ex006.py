#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n = int(input("digite um numero"))
r = int(n*2)
r2 = int(n*3)
r3 = float(n**(1/2))

print('o dobro de', n, 'é', r, 'e o triplo de', n, 'é', r2, 'e a raiz quadrada de', n, 'é', r3)

#ou

n = int(input('digite um numero'))
d = n*2
t = n*3
r = n**(1/2)

print('O dobro do numero é {} o triplo é {} e a raiz quadrada é {:.2f}'.format(n, d, t, r))