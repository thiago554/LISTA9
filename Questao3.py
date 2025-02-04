nota1 = float(input('digite a sua primeira nota: '))
nota2 = float(input('digite a sua segunda nota: ' ))


peso1 = int(input('digite o peso da primeira nota: '))
peso2 = int(input('digite  o peso da segunda nota: '))


media = ((nota1*peso1) + (nota2*peso2))/(peso1+peso2)
print(f'a media ponderada das nota é: {media}')
