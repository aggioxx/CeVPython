from random import randint


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)


