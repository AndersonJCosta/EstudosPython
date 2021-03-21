
from math import sin,cos,tan,radians
grau=float(input('Digite o grau '))
print('Para o grau {:.2f} \nO seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}'
      .format(grau,
              sin(radians(grau)),
              cos(radians(grau)),
              tan(radians(grau))))
'''

====================================================
from math import sin,cos,tan,radians,degrees
grau=radians(float(input('Digite o grau para o calculo ')))
seno=sin(grau)
coseno=cos(grau)
tangente=tan(grau)
print('para o grau {:.2f}\nO seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}'.format(degrees(grau),seno,coseno,tangente))
====================================================
import math
g=float(input('Digite o grau para o calculo '))
s=math.sin(math.radians(g))
c=math.cos(math.radians(g))
t=math.tan(math.radians(g))
print('Para o grau {}\no seno é {:.2f}\no coseno é {:.2f}\ne a tangente é {:.2f}'.format(g,s,c,t))
'''
