num = int(input('Quantos termos voce quer mostrar? '))
print ('-' * 30)
t1 = 0
t2 = 1
nt = 0
cont = 1
while cont <= num:
    nt = t1 + t2
    t1 = t2
    t2 = nt
    cont += 1
    print ('{}  '.format(nt), end='')
