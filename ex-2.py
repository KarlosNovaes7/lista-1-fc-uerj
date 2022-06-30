
a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))

n = 5

for termo in range(n):
    print(a1 + r*termo, end=" ") #isso é igual a a1 + r vezes ((n-1) = index)

print('\n')

for termo in range(a1, a1+n*r, r): #range = onde começa + onde termina + de quanto em quanto
    print(termo, end=" ")

print('\n')

for loopPa in range(n): 
    print(a1, end=" ")
    a1 +=3 

