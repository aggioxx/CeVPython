nums = []
for cont in range(0,5):
    nums.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'O maior valor digitado foi {max(nums)}, na posição', end = '')
for c, v in enumerate(nums):
    if v == max(nums):
        print(f'{c}...', end='')
print(f'O menor valor digitado foi {min(nums)}, na posição ',end='')
for c, v in enumerate(nums):
    if v == min (nums):
        print(f'{c} ', end='')

