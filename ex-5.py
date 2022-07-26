somaDosPesos = 0

for numeroCaixa in range(1, 26):
    pesoCaixa = float(input('Digite o peso da caixa ' + str(numeroCaixa) + ': ' ))
    somaDosPesos += pesoCaixa
    
print('A soma dos pesos de todas as caixas é:', somaDosPesos)
