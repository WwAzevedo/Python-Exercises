#Esse programa cadastra uma lista de trabalhadores/salarios.
#No final mostra quem é o trabalhor com o maior salario e quem ganha abaixo de R$1000.

trabalhadores = []
salario = []
maior_salario = 0


for i in range(5):
    trabalhadores.append(input("Qual o nome do trabalhador: "))
    salario.append(float(eval(input("Qual o salario do trabalhador " + trabalhadores[i] + ":"))))

    if salario[i] > maior_salario:
        maior_salario = salario[i]
        
for i in range(len(trabalhadores)):

    if salario[i] == maior_salario:
        print("O trabalhador com o maior salario é ", trabalhadores[i])

for i in range(len(trabalhadores)):
    if salario[i] < 1000:
        print("Trabalhador com salario inferior a 1000: ", trabalhadores[i])
