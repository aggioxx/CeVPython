import random
escolha = random.randint(1, 3)
ppt = int(input('Escolha sua jogada:\n [1]Pedra\n [2]Papel\n [3]Tesoura\n Escolha sua jogada:'))

if escolha == 1 and ppt == 1:
    print('PEDRA X PEDRA')
    print('Ninguem ganhou e ninguem perdeu')
elif escolha == 1 and ppt == 2:
    print('PEDRA X PAPEL')
    print('Vc ganhou da maquina, parabens')
elif escolha == 1 and ppt == 3:
    print('PEDRA X TESOURA')
    print('A maquina te deu um pau, chora lixo')
elif escolha == 2 and ppt == 1:
    print('PAPEL X PEDRA')
    print('A maquina te deu um pau, chora lixo')
elif escolha == 2 and ppt == 2:
    print('PAPEL X PAPEL')
    print('Ninguem ganhou e ninguem perdeu')
elif escolha == 2 and ppt == 3:
    print('PAPEL X TESOURA')
    print('Vc ganhou da maquina, parabens')
elif escolha == 3 and ppt == 1:
    print('TESOURA X PEDRA')
    print('Vc dominou a maquina, parabens')
elif escolha == 3 and ppt == 2:
    print('TESOURA X PAPEL')
    print('A maquina te dominou, chora marreco')
elif escolha == 3 and ppt == 3:
    print('TESOURA X TESOURA')
    print('Empata y Empata')
else:
    print('Digita um numero ai parca')
