lista = ('PYTHON','ALEXA','AMAZON','CURSO','GUILHERME',
        'NICOLE','GATA','GOSTOSA','MUSA',
        'BUNDA','GRANDE','PROGRAMAR','TRABAIA','BANCO','ITAU',
        'FEITO','COM','VOCE')
for p in lista:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end='')