aluno = input("Qual o nome do aluno?")
n1 = float(input("Nota primeiro semêstre:"))
n2 = float(input("Nota segundo semêstre:"))
n3 = float(input("Nota terceiro semêstre:"))
n4 = float(input("Nota quarto semêstre:"))
resultado = (n1 + n2 + n3 + n4)/4


if resultado >= 5:
    print("Sua média final foi", resultado ,"APROVADO")
else:
    print("Sua média final foi", resultado ,"REPROVADO")
    
