preco = float(input('digite preco atual do produto: '))
desconto = float(input('digite o desconto do produto: '))


valor = preco - (preco*desconto/100)


print('o valor final que deve pagar e de: ', valor)
