pesoTotalCaixas = 0

for i in range(1, 26):
    numeroCaixa = i
    input('Digite o peso da caixa ' + str(numeroCaixa) + ': ' )
    somaDosPesos = pesoTotalCaixas + i

print('A soma dos pesos de todas as caixas é:', somaDosPesos)
