nums = [[], []]
while True:
    dig = int(input('Digite um número: '))
    if dig % 2 == 0:
        nums[0].append(dig)
    else:
        nums[1].append(dig)
    esc = str(input('Deseja continuar? [S/N]')).lower().strip()
    if esc == 'n':
        break
nums[0].sort()
nums[1].sort()
print(f'Os números pares digitados foram {nums[0]}')
print(f'Os números ímpares digitados foram {nums[1]}')

