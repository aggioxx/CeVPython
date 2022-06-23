#incremento percentual
sal = float(input('Digite o Salario de seu funcionario: '))
aum = float(input('Digite a porcentagem do aumento: '))
#calc = (sal * aum) / 100
#ns = sal + calc (fiz assim)
nsatt = sal + (sal * aum / 100)
print('O novo salario e: {}'.format(nsatt))
