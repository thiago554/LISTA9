import random
x = random.randint(1,100)
for j in range(1, 999):
   t = int(input('tente acertar um numero de um a cem: '))
   if t != x:
       if (x -t)<0:
           t = (t* -1)
       if (x-t)<10:
           print('está quase la')
       elif (x-t)<30:
           print('esta frio')
       else:
           print('esta muito frio')
   else:
       print(f'acertou o numero era {x}')
