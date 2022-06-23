def cont(*num):
    print('=' * 40)
    print(f'Os valores digitados foram: {num}. Um total de {len(num)} valores')
    print(f'O maior valor digitado foi {max(num)}')
    print('=' * 40)


cont(1, 5, 7, 9, 8, 5)