#Crie um algoritmo que leia um número e mostre
#o seu dobro, triplo e raíz quadrada.

n=int(input('Digite um número:'))
d=n*2
t=n*3
r=n**(1/2)
print('O dobro de {} vale {}.'.format(n,d))
print('O triplo de {} vale {}. \n A raíz quadrada de {} é igual a {:.2f}.'.format(n,t,n,r))
