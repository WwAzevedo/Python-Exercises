s1 = int(input("Qual o numero SOBRE a equação:"))
x1 = int(input("Qual o PRIMEIRO numero com X:"))
x2 = int(input("Qual o SEGUNDO numero com X:"))
x3 = int(input("Qual o TERCEIRO numero com X:"))
d1 = int(input("Qual o valor da PRIMEIRA distributiva:"))
v1 = int(input("Qual o valor do PRIMERO numero em parenteces:"))
d2 = int(input("Qual o valor da SEGUNDA distributiva:"))
v2 = int(input("Qual o valor do SEGUNDO numero em parenteces: "))
i1 = int(input("Qual o valor inteiro depois do IGUAL: "))


p1x = d1*x1
p2 = d1*v1

p3x = d2*x2
p4 = d2*v2

p5x = x3+(p1x-p3x)
p6 = p4-p2

p7 = p6/p5x

if p7 % 1:
    r1 = p6/2
    r2 = p5x/2
    print(p1x,p2,"=",p3x,p4)
    print(p5x,"=",p6)
    print(r1,"/",r2)
else:
    print(p1x,p2,"=",p3x,p4)
    print(p5x,"=",p6)
    print(p7)
