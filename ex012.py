#Desconto percentual
p = float(input('Digite o preco do produto: '))
vd = float(input('Digite a porcentagem de desconto: '))
#desc = (p * vd) / 100
#res = p - desc (forma que eu fiz antes)
desc = p - (p * vd / 100) #correcao da aula
print('O novo preco do produto com desconto e: {}'.format(desc))

