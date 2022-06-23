print('{:=^40}'.format('Aliexpress da Bahia'))
preco = float(input('Qual o valor total da compra? '))
pag = int(input('Qual a forma de pagamento?\n [1] A vista\n [2] A vista no cartao\n [3] Ate 2x no cartao\n [4] 3x ou mais\n DIGITE SUA OPCAO '))

if pag == 1:
    print('O total a ser pago  com 10%` e: R${:.2f}'.format(preco - (preco * 10) / 100))
elif pag == 2:
    print('O total a ser pago com 5%` e R${:.2f}'.format(preco - (preco * 5) / 100))
elif pag == 3:
    print('O total a ser pago e R${}'.format(preco ))
else:
    print('O total a ser pago com juros e R${:.2f}'.format(preco + (preco * 20) / 100))