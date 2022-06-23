km = int(input('Qual a velocidade seu carro passou no radar? '))
if km <= 80:
    print('Ta tranquilo meu querido, vc se safou dessa')
else:
    print('Xiiiii, se prepara que la vem paulada, sim voce foi multado em: {} '.format((km - 80) * 7))
    