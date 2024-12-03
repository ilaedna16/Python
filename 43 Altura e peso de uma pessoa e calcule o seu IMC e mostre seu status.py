#Desenvolva uma lógica que leia o peso e altura de uma pessoa,
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:;
#Abaixo de 18.5: abaixo do peso
#entre 18.5 e 25: peso ideal
#25 até 30: sobrepeso
#30 até 40: obesidade
#Acima de 40: obesidade mórbida

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa de peso normal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso')
elif 30 <= imc < 40:
    print('Você está em obesidade!')
elif imc >= 40:
    print('Você está em obesidade mórbida, cuidado!')

