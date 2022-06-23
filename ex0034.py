sal = int(input('Digite o salario do funcinário: '))
if sal <=1250:
    print('O novo salario fica 15% maior, ou seja R${}'.format((sal * 15 / 100) + sal))
else:
    print('O salario fica 10% maior, ou exatamente R${}'.format((sal * 10 / 100) + sal))