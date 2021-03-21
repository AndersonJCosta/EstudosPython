km=float(input('Quilometros percorrido = '))
dias=int(input('Dias de uso = '))
preço=(60*dias)+(0.15*km)
#60/dia e 0,15/km
print('O valor da locação é da R${:.2f}'.format(preço))
print('preço {:.2f}'.format(km*0.15+dias*60))
print('Tudo bem')
