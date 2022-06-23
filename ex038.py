num1 = int(input('Digite o primeiro numero inteiro: '))
num2 = int(input('Digite o segundo numero inteiro: '))

if num1 > num2:
    print('{} é maior que {}, logo o primeiro valor é o maior'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}, logo o segundo valor é o maior'.format(num2, num1))
else:
    print('Nao existe valor maior, os dois sao iguais')

