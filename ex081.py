nums = []
cont = 1
while True:
    nums.append(int(input(f'Digite o {cont}º valor: ')))
    cont += 1
    esc = str(input('Deseja continuar? [S/N] ').lower().strip())
    if esc == 'n':
        break
nums.sort(reverse=True)
print(nums)
if 5 in nums:
    print('O número 5 foi digitado')
else:
    print('O 5 não está nesse rolo não')