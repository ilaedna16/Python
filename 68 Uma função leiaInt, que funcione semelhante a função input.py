#Cie um programa que tenha a funçaõ leiaInt(), que vai funcionar
#de forma semelhante á função input() do python, só que fazendo a validação
#para aceitar apenas um valor numérico.

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\003[m')
        if ok:
            break
    return valor

#programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')



