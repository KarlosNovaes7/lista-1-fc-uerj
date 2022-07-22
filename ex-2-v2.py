
primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
numeroDeTermos = int(input("Digite o numero de termos: "))

# 10,20,30,40, ...
# r = 10

for i in range(numeroDeTermos):
    print(primeiroTermo)
    primeiroTermo = primeiroTermo + razao
