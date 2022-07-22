# Crie um algoritmo que leia uma quantidade não determinada de números inteiros.

# O programa deve calcular e escrever a quantidade de números pares e ímpares e

# a média aritmética dos números pares.

# A leitura deve ser encerrada quando for lido o número zero, que não deve ser considerado

quantidadePares = 0
quantidadeImpares = 0

somaNumerosPares = 0

while(True):
    numero = int(input("Coloque o numero desejado:"))
    if(numero == 0):
        break
    if(numero % 2 == 0):
        quantidadePares = quantidadePares + 1
        somaNumerosPares = somaNumerosPares + numero
    else:
        quantidadeImpares = quantidadeImpares + 1
        
print('A quantidade de numeros paress é:', quantidadePares)
print('A quantidade de numeros impares é:', quantidadeImpares)

if(quantidadePares != 0):
    mediaAritmetica = somaNumerosPares/quantidadePares
    print('A media aritmetica dos pares é:', mediaAritmetica)
else:
    print('Nenhum par encontrado para a média aritmética')

