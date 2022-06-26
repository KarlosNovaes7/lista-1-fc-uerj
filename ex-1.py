# 1p = ter input para receber os dados
# 2p = uma função que de a media salarial de acordo com o sexo e retornar o resultado
# 3p = maior salario encontrado desde que a idade seja menor que 30 anos

data = []

while(True):

    while(True):
        age = int(input('Qual é sua idade? (em número apenas e maior de 16 anos) '))
        if (age < 0 or age >= 16):
            break
        print('a idade é menor que o critério estabelecido, tente novamente')

    if (age < 0):
        break

    while(True):
        sex = str(input('Qual é seu sexo? ("feminino" ou "masculino") '))
        if (sex == "feminino" or sex == "masculino"):
            break
        print('sexo não encontrado, tente novamente')

    while(True):
        wage = float(
            input('Qual é seu salário? (em números apenas, sem ponto ou vírgula) ')
        )
        if (wage > 0):
            break
        print('digite um salário válido')

    data.append([age, sex, wage])

# sum = guarda Salário e a quantidade de salários
sumWageF = []
sumWageM = []
maxWage = 0

for person in data:
    if (person[1] == 'feminino'):
        sumWageF.append(person[2])
    else:
        sumWageM.append(person[2])
    if (person[0] < 30 and maxWage < person[2]):
        maxWage = person[2]

if (len(sumWageF) != 0):
    print('a média salarial das mulheres é:',
          round(sum(sumWageF) / len(sumWageF), 2))
else:
    print('infelizmente não temos dados para a média salarial das mulheres')

if (len(sumWageM) != 0):
    print('a média salarial dos homens é:',
          round(sum(sumWageM) / len(sumWageM), 2))
else:
    print('infelizmente não temos dados para a média salarial dos homens')

print('o maior salário entre pessoas abaixo de 30 anos é:', maxWage)
