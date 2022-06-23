import math
vlrcasa = float(input('Digite o valor da casa que vc escolheu: '))
sal = float(input('Qual o valor mensal do seu salario? '))
time = int(input('Em quantos anos voce pretende pagar essa casa? '))

calc = vlrcasa / (time * 12)
calc2 = sal * 30 / 100

if calc <= calc2:
    print('O valor total das parcelas sera de R${:.2f} para pagar em {} anos. \n APROVADO'.format(calc, time)) 

else:
    print('Voce nao pode comprar essa casa, a parcela de R${:.2f} em {} anos compromete mais que 30%" de sua renda.\n EMPRESTIMO NEGADO'.format(calc, time))