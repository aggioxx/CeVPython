from random import random


import random
ale = random.randint(1, 5)
advinha = int(input('Tente advinhar o numero entre 1 e 5 que o computador escolheu: '))
if advinha == ale:
    print('Parabens, o numero {} foi mesmo o que o computador escolheu. Voce doutrinou a maquina!!!!'.format(ale))
else: 
    print('Xiiiiiiiiii, a maquina venceu dessa vez. O computador escolheu o numero {}'.format(ale))