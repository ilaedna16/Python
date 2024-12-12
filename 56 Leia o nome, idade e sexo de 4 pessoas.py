#Desenvolva um programa que leia o nome, idade e sexo de 4 pesssoas.
#No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homen mais velho.
#Quantas mulheres tem menos de 20 anos.

somaidade = 0
médiaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioidadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homen mais velho tem {} anos e se chama {}.'.format(maioridadehomen, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))


