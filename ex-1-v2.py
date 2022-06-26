#exemplo de dicionario = dic

data = []

while(True):
    while(True):
        age = int(input('Qual é sua idade? (em número apenas e maior de 16 anos) '))
        if (age < 0 or (16 <= age < 120)):
            break
        print('a idade é menor que o critério estabelecido, tente novamente')

    if (age < 0):
        break

    while(True):
        sex = str(input('Qual é seu sexo? ("F" ou "M") '))
        if (sex == "F" or sex == "M"):
            break
        print('sexo não encontrado, tente novamente')

    while(True):
        wage = float(
            input('Qual é seu salário? (em números apenas, sem ponto ou vírgula) ')
        )
        if (wage > 0):
            break
        print('digite um salário válido')

    data.append({"age": age, "sex": sex, "wage": wage})

for person in data:
    print(person["age"])
