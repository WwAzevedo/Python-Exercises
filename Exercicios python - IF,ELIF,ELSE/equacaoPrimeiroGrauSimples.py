x = int(input("insira o valor com x:"))
esquerda = int(input("Insira o numero ANTES do = :"))
direita = int(input("Insira o numero DEPOIS do = :"))

passo1 = direita - esquerda

resultado = passo1 / x

print(x,"x", esquerda,"=",direita)
print(x,"x=",direita,esquerda)
print("x=",passo1,"/",x)
print("o resultado da equação é:", resultado)
                
