frase = input('Digite uma frase ')
'''fatimento de strings'''
print(frase)

print('O 10° caracter é = ',frase[9])

print('Do 10° ao 13° é = ',frase[9:13])

print('Até o 5º é = ',frase[:5])

print('Partindo do 10, de 3 em 3 = ',frase[9::3])

print('A frase tem ',len(frase),' caracteres')

print('A frase tem ',frase.count('o'),' leta(s) o')

print('So do 1° ao 13° tem = ',frase.count('o',0,13),' letras(s) o') #mostra quantas vezes encontou o 'o' no intervalo de 0 a 13 (o 13° é será incluido)

print('O primeiro "deo" está na posição = ',frase.find('deo'),'(-1 para não encontrado)') #mostra onde ele encontou o 'deo'

'''
o operador "in" retorna se exite uma sequencia entro da frase

"frase está como exemplo de de variavel"

frase.replace('Python','Android') # troca 'Python' por 'Android' 
frase.upper() #torna letras para maiurculas
frase.lower() #torna letras minusculas
frase.captalizer() #só a primeira em maiusculo
frase.title() #primeira de cada palavra em maiusculo
frase.strip() #remove espaços no inicio e fim da string
frase.split() #divide pelos espeços uma string em uma lista com varios elementos
'-'.join(frase) reune a lista separando por '-'

'''
