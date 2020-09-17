# Esse programa cadastra o nome/nota dos alunos e no final mostra quem foi aprovado ou reprovado.

nomes = []
notas = []
soma = 0

print("##### CADASTRO DE NOTAS #####")
for i in range(10):
    nomes.append(input("Informe o nome do aluno:"))
    notas.append(float(eval(input("Qual o nota do aluno " + nomes[i] + ":"))))

    soma = soma + notas[i]

media = soma / 10

for i in range(len(nomes)):
    if notas [i] > media:
        print(nomes[i],"Parabéns, você foi aprovado!\n")
    else:
        print(nomes[i],"Você não obteve a nota minima. :(\n")
