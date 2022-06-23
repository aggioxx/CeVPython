times = ('Atletico MG', 'Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense','América MG','Atlético GO','santos', 'Ceará','Internacional','São Paulo',
'Atlético PR','Cuiabá','Juventude','Gremio','Bahia','sport','Chapecoense')
print(f'Os 5 primeiros colocados foram {times[0:5]}')
print(f'Os ultimos 4 colocados foram{times[16:20]}')
print(f'Os times em ordem alfabetica sao {sorted(times)}')
print(f'A Chapecoense esta na posicao {times.index("Chapecoense")+1}')