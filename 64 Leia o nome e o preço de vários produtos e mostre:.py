#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:
#Qual é o total gasto na conta.
#Quantos produtos custam mais de R$1000.
#Qual é o nome do produto mais barato.

total = totmil = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont = cont + 1
    total = total + preço
    if preço > 1000:
        totmil = totmil + 1
    if cont == 1:
         menor = preço
         barato = produto
    else:
         if preço < menor:
             menor = preço
             barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do Programa '))
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato custa R${menor:.2f}')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
