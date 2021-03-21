co=float(input('Digite o cateto o posto '))
ca=float(input('Digite o cateto adjacente '))
from math import sqrt
h=sqrt(co**2+ca**2)
print('A hipotenisa dos catetos {} e {} é {:.2f}'.format(co,ca,h))
