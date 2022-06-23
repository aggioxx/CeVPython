frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} è {}'.format(junto, inverso))
#primeiro -1 = comeca pela ultima posicao
# segundo -1 = vai ate o comeco
# terceiro -1 voltando de 1 em 1 letra
if inverso == junto:
    print('Cha ching, temos um palindromo')
else:
    print('No eres un palindromo')
