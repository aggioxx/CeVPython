todos = []
par = []
impar = [] 
while True:
    nums = int(input(f'Digite um valor: '))
    todos.append(nums)
    esc = str(input('Quer continuar? [S/N] ')).strip()[0]
    if nums % 2 == 0:
        par.append(nums)
    else:
        impar.append(nums)
    while esc not in 'SsNn':
        esc = str(input('Resposta inválida, deseja continuar? [S/N]')).strip()[0]
    if esc == 'n':
        break
print(todos)
print(par)
print(impar)