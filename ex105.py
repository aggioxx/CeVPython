def notas(*num, sit=False):
    mr = dict()
    mr['total'] = len(num)
    mr['maior'] = max(num)
    mr['menor'] = min(num)
    mr['media'] = sum(num) / len(num)

    if sit == True and mr['media'] < 5:
        mr['situacao'] = 'RUIM'
    elif sit == True and mr['media'] >= 5 and mr['media'] <=7:
        mr['situacao'] = 'Razoável '
    elif sit == True and mr['media'] > 7:
        mr['situacao'] = 'Ruim'
            
    return mr


resp = notas(5.5, 5.5, 5, sit=True)
print(resp)
help(notas)

