#Escreva um programa que pergunte o salário de um funcionário
#e calcule o valor do seu aumento.
#Para salários superiores a RS1.250.00. Calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
