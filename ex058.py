from random import randint
pc = randint(1, 11)
user = int(input('Digite um numero: '))
while user != pc:
    user = int(input('Voce errou, tente novamente: '))

print('Sim, voce acertou. O PC escolheu o numero {}'.format(pc))