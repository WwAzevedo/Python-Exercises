n1 = int(input("Insira o primeiro valor:"))
n2 = int(input("Insira o segundo valor:"))
op = input("Qual operação realizar?")

if op == "+":
    soma = n1 + n2
    print(soma)
elif op == "-":
    menos = n1 - n2
    print(menos)
elif op == "*":
    mult = n1 * n2
    print(mult)
elif op == "/":
    div = n1 / n2
    print(div)
else:
    print("Insira + para soma, - para subtração, * para multiplicação, / para divisão")

 
