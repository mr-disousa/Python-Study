# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Para criar sua tabuada, Digite um numero: '))
r1 = n*0
r2 = n*1
r3 = n*2
r4 = n*3
r5 = n*4
r6 = n*5
r7 = n*6
r8 = n*7
r9 = n*8
r10 = n*9
r11 = n*10

print('A tabuada do numero informado é',
n,'x 0 =',r1,
n,'x 1 =',r2,
n,'x 2 =',r3,
n,'x 3 =',r4,
n,'x 4 =',r5,
n,'x 5 =',r6,
n,'x 6 =',r7,
n,'x 7 =',r8,
n,'x 8 =',r9,
n,'x 9 =',r10,
n,'x 10 =',r11)


#ou

n = int(input('Digite um numero e veja a sua tabuada'))
print('{} x {:2} = {}'.format(n, 0, n*0))
print('{} x {:2} = {}'.format(n, 1, n*1))



