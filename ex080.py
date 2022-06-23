lis = [ ]
for c in range(1, 6):
    n = int(input(f'Digite o {c}° número: '))
    if c == 1 or n >= lis[-1]:
        lis.append(n)
    elif n <= lis[0]:
        lis.insert(0, n)
    elif lis[0] <= n <= lis[1]:
        lis.insert(1, n)
    elif lis[1] <= n <= lis[2]:
        lis.insert(2, n)
    elif lis[2] <= n <= lis[3]:
        lis.insert(3, n)
print(lis)