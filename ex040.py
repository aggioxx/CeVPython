n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2

if m < 5:
    print('REPROVADOOOOOOOO')
elif m == 5 and m < 6.9:
    print('Voce ta de recuperacao, ainda tem uma chance, saiba usar')
else:
    print('Vai pra casa, vc esta de feriaas garotinho')
