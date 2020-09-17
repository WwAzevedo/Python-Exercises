import math
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

d = (b**2) - 4 * a * c

if d >0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)

print ("Seus resultados são:",x1, "e", x2,)
