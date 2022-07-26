gastoTotal = 0

for numeroProduto in range(1, 51):
    quantidadeProduto = int(input('Digite a quantidade do ' + str(numeroProduto) + 'º produto '))
    precoProduto = int(input('Digite o preço do ' + str(numeroProduto) + 'º produto '))

    gasto = quantidadeProduto * precoProduto
    gastoTotal += gasto

print('O total gasto foi:', gastoTotal)
