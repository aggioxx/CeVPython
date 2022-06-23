#Area de uma parede + qtde de tinta para pintar
alt = float(input('Qual a altura da parede: '))
lar = float(input('Qual a largura da parede: '))
mquad = alt * lar
qtdeTinta = mquad / 2
print ('A parede tem uma area de {}m², sendo assim {}L de tinta sao necessarios para pinta-la'.format(mquad, qtdeTinta))
