l=float(input('Largura em metros = '))
a=float(input('Altura em metros = '))
area=l*a
print('Sua parede de {:.2f}m por {:.2f}m tem uma área de {:.2f}m²'.format(l,a,area))
tinta=area/2
print('Para pintar {:.2f}m²'.format(area))
print('É necessário {:.2f} litros de tinta'.format(tinta))
#Tinta pinta 2m²/l