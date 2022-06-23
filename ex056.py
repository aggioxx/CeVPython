sidade = 0
idvelho = 0
velho = ''
mulheres = 0
for c in range (1, 5):
    nome = str(input('Digite o nome da pessoa {}: '.format(c))).strip()
    idade = int(input('Digite a idade da pessoa {}: '.format(c)))
    sexo = int(input('Selecione seu sexo: \n[1] Masculino \n[2] Feminino\n '))
    
    sidade += idade
    if sexo == 2 and idade <=20:
        mulheres += 1
    if c == 1 and sexo == 1:
        velho = nome
        idvelho = idade
    else:
        if sexo == 1 and idvelho < idade: 
            idvelho = idade
            velho = nome
    
midade = sidade / 4
print('A media de idade do grupo é {}, o homem mais velho é o {} e temos {} mulheres com menos de 20 anos'.format(midade, velho, mulheres))