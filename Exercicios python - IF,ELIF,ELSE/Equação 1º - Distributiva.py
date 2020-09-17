d1 = int(input("Qual o valor da PRIMERA distributiva:"))
v1 = int(input("Qual o valor do PRIMERO numero em parênteses:"))
v2 = int(input("Qual o valor do SEGUNDO numero em parênteses:"))
d2 = int(input("Qual o valor da SEGUNDA distributiva:"))
v3 = int(input("Qual o valor do PRIMERO numero em parênteses:"))
v4 = int(input("Qual o valor do SEGUNDO numero em parênteses:"))
r1 = int(input("Qual o valor DEPOIS do = :"))

p1 = d1*v1
p2 = d1*v2

p3 = d2*v3
p4 = d2*v4

p5 = p2+p4
p6 = r1-p1
p7 = p6-p3

resultado = p7/p5

print(p1,p2,p3,p4,r1)
print(p5,"=",p7)
print("O valor de X é ",resultado)
