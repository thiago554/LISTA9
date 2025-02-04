contador = 0


frase = input('digite uma frase: ')
for j in list(frase):
   if j =='a'or j =='e'or j == 'i' or j =='o' or j =='u':
       contador +=1


print(f'a quantidade de vogais na frase é de : {contador}')
