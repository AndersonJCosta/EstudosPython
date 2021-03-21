
# 4 principais classes de variaveis

#int(7, -4, 0 , 9875)
#float(4.5, 0.076, -15.223, 7.0)
#bool(True,False)
#str('Olá','7.5','')
#print('A soma vale{}'.format(s))


n1=input('Digite um número: ')          #primeiro número entrou com str
n2=int(input('Digite outro número'))    #segundo número entrou como int
print(type(n1))                         #imprimi o tipo da variavel n1
s=int(n1)+(n2)                          #transforma n1 em int e soma com n2
print('A soma vale',s)                  #mostra a soma entre n1 e n2

print('A soma entre',n1,'e',n2,'vale',s)
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
print('teste {}'.format(n2+n2))
print(n1.isnumeric())
print('ok')
print(type(n2))