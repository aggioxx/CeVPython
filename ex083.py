mat = str(input('Digite sua expressão matemática: '))
pilha = [] #stack, empilhados
for simb in mat:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simb)
            break
if len(pilha) == 0:
    print('BELEEEEEEEEEEEEEEEEZA, sua expressão tá certinha')
else:
    print('Xiiiii, dá uma revisada, a expressão não tá certa')

