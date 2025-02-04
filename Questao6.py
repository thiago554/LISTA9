ímpares = 0
pares = 0


for j in range(1, 11):
   t = int(input('digite um numero inteiro(10 no total): '))
   if t%2==0:
       pares +=1
   else:
       impares +=1
print(f'nume ros pares no total: {pares}\nnumeros impares no total: {impares}')
