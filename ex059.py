from time import sleep
c = 0
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
while c != 5:
    c = int(input('\nSelecione a opcao desejada:\n [1]Somar\n [2]Multiplicar\n [3]Maior\n [4]Novos numeros\n [5]\033[1;31mSair do programa\n \033[0mDigite sua escolha: '))
    if c == 1:
        print(n1 + n2)
    elif c == 2:
        print(n1 * n2)
    elif c == 3:
        if n1 > n2:
            print('{} eres major que {}'.format(n1, n2))
        else:
            print('{} eres major que {}'.format(n2, n1))
    elif c == 4:
        print('Informe os numeros novamente')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif c == 5: 
        print('Xau xau')   
    else: 
        print('Invalido. Tente novamente')
    sleep(2)
print('Fim da linha')