nomes = []


a=0
b=0
for j in range(5):
   a+=1
   nome = input(f'digite um nome: ({a/5}\n')
   if nome[0]=='a':
       nomes.append(nome)
       b+=1
       print(f'a quantidade de nomes que comçam com a letra "a": {b}')
       if nomes !=[]:
           print(nomes)
