cont = ('zero','Um', 'dois','tres','quatro','cinco','seis','sete', 'oito', 'nove','dez', 'onze', 'doze', 'treze','catorze','quinze','dezesseis', 'dezessete', 'dezenove', 'vinte')
num = 21
while num not in range (0, 20):
    num = int(input('Digite um numero inteiro entre 0 e 20: '))
print(cont[num])