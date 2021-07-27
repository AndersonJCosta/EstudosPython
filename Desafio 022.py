'''

Recebe o nome
retorna o nome em maiusculo
retorna o nome em ninusculo
retorna quantidade de letras do nome (não conta espeços)
retorna quantidade de letras do primeiro nome
'''

Nome = input('Digite seu nome completo ')
print(Nome.upper())
print(Nome.lower())
print('O nome contem ',len(''.join(Nome.split())),' letras')
dividido=Nome.split()
print('O primeiro nome tem ',len(dividido[0]),' letras')
