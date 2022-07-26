
nomeProduto = input('digite o nome do produto: ')
produtoMaisCaro = 0
nomeProdutoMaisCaro = ""
precoProduto = 0

while(nomeProduto != 'xxx'):
    precoProduto = float(input('digite o preço do produto: '))
    if (precoProduto > produtoMaisCaro):
        produtoMaisCaro = precoProduto
        nomeProdutoMaisCaro = nomeProduto
    nomeProduto = input('digite o nome do produto: ')



print("Nome do produto mais caro", nomeProdutoMaisCaro)
print('Produto mais caro', produtoMaisCaro)
