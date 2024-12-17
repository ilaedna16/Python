#Crie um programa que leia vários números inteiros pelo teclado.
#o programa só vai parar quando o usuário digitar o valor 999. que
#é a condição da parada. No final, mostre quantos números foram
#digitados e qual foi a soma entre elas.

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma = soma + núm
    cont = cont + 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
