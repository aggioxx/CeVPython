num = int(input('Digite um numero inteiro: '))
escolha = int(input('Selecione a base que voce deseja converter:\n [1] Binario\n [2] Octal\n [3] Hexadecimal\n Digite sua escolha: '))
if escolha == 1:   
    print('O numero {} em binario resulta em {}'.format(num, bin(num)[2:]))
elif escolha ==2:
    print('O numero {} em octal resulta em {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O numero {} em hexadecimal resulta em {}'.format(num, hex(num)[2:]))
else:
    print('{} nao foi uma das opcoes, digite uma opcao valida'.format(num))



