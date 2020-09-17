print("Lançamento de Notas - Escola de Inglês JoWell Sant’ana\n")
print("**************Alunos Impares**************")
aluno = 1
soma = 0
cont = 0
for impar in range(1,50,2):
    impar = float(input("Insira a nota do aluno Nº{}: ".format(aluno)))
    aluno = aluno + 2
    soma = soma + impar
    cont = cont + 1
    mediaImpares = soma / cont

print("\nA media dos alunos IMPARES é {}\n".format(mediaImpares))


print("**************Alunos Pares**************")
aluno = 2
soma = 0
cont = 0
for par in range(2,51,2):
    par = float(input("Insira a nota do aluno Nº{}: ".format(aluno)))
    aluno = aluno + 2
    soma = soma + par
    cont = cont + 1
    mediaPares = soma / cont

print("\nA media dos alunos PARES é {}\n".format(mediaPares))

if mediaImpares > mediaPares:
    print("*************************************")
    print("A maior media foi dos alunos Impares!")
    print("*************************************")
else:
    print("***********************************")
    print("A maior media foi dos alunos Pares!")
    print("***********************************")
