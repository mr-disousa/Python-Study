
n1 = int(input('digite um valor'))
n2 = int(input('digite outro'))
s = n1+n2

#formato antigo#
print('A soma entre', n1, 'e', n2, 'vale',s)

#formatando para um jeito mais facil#

print('A soma entre {} e {} vale {}' .format(n1, n2,s) )


# Crie um programa que leia dois numeros e mostre a soma entre eles.

n1 = int(input('digite um numero:'))
n2 = int(input('digite outro:'))
s = n1+n2
print('A soma de {} e {} é {}' .format(n1, n2, s))
