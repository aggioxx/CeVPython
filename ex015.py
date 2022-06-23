#Aluguel de carro
dia = int(input('Qauntos dias voce usou o carro? '))
km = float(input('Quantos KM voce rodou com o carro? '))
pfinal = (dia * 60) + (km * 0.15)
print ('O valor final deu R${:.2f}'.format(pfinal))