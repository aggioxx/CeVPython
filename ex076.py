lista = ('Memória RAM', 299,
         'Placa de vídeo', 3200,
         'Fonte', 600,
         'HD', 300,
         'SSD', 400,
         'Gabinete', 200,
         'Fans', 150,
         'WaterColeer', 500,
         'Placa mãe', 799,
         'Ryzen', 1599)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
         print(f'{lista[pos]:-<30}', end = '')
    else:
        print(f'R${lista[pos]:>5.2f}')
    
