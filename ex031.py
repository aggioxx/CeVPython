rodado = float(input('Quantos km voce vai viajar? '))
if rodado <=200.0:
    print('Voce vai pagar R${:.2f} na sua passagem'.format(rodado * 0.50 ))
else:
    print('Voce vai pagar R${:.2f} na sua passagem'. format(rodado *0.45))