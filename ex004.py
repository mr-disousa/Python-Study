# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

a = input('digite alguma coisa')
print(type(a))
print('é alfabetico?', a.isalpha())
print('é alfanumerico?', a.isalnum())
print('é ', a.istitle())
print('é numerico?', a.isnumeric())



