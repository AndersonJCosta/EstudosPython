
#Operadores aritiméticos

n1=int(input('Primeiro número'))
n2=int(input('Segundo número'))
print(        'Soma = {}\nSubtração = {}\nMultiplicação = {}\nDivisão = {:.3f}\nExponenciação = {}\nDivisão inteira = {}\nResto da divisão = {}'
      .format(n1+n2,      n1-n2,          n1*n2,              n1/n2,        n1**n2,             n1//n2,               n1%n2))

# + adição
# - subtração
# * multiplicação
# / divisão
# ** exponenciação
#                exponenciação pode ser feito com função interna "pow()" mas
# // disvisão inteira
# % resto da divisão

#orden de precedencia
# 1° ()
# 2° **
# 3° * , / , // , %
# 4º + , -
# Qando houver mais de uma operação com a mesma precedencia, opera que aparecer primeiro
