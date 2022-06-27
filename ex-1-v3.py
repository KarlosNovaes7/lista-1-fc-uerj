#exemplo com classe

class Person:
  def __init__(self, age, sex, wage):
    self.age = age
    self.sex = sex
    self.wage = wage

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
        if (sex.upper() == "F" or sex.upper() == "M"):
            break
        print('sexo não encontrado, tente novamente')

    while(True):
        wage = float(
            input('Qual é seu salário? (em números apenas, sem ponto ou vírgula) ')
        )
        if (wage > 0):
            break
        print('digite um salário válido')

    p = Person(age, sex, wage)
    data.append(p)

sumWageF = []
sumWageM = []
maxWage = 0

for person in data:
    if (person.sex.upper() == 'F'):
      sumWageF.append(person.wage)
    else:
      sumWageM.append(person.wage)
    if (person.age < 30 and maxWage < person.wage):
      maxWage = person.wage

def awageAverage(wage):
    return round(sum(wage) / len(wage))

def sentences():
    if (len(sumWageF) != 0):
        print('a média salarial das mulheres é:', awageAverage(sumWageF))
    else:
        print('infelizmente não temos dados para a média salarial das mulheres')

    if (len(sumWageM) != 0):
        print('a média salarial dos homens é:', awageAverage(sumWageM))
    else:
        print('infelizmente não temos dados para a média salarial dos homens')

    print('o maior salário entre pessoas abaixo de 30 anos é:', round(maxWage))

sentences()
