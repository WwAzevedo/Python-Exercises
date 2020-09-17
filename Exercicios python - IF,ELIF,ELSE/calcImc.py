print("*********CALCULO IMC*********")

peso = float(input("Insira o seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso / (altura**2)

if imc < 16:
    print("Baixo peso Grau III")
elif imc == 16 or imc < 16.99:
    print("Baixo peso Grau II")
elif imc == 17 or imc < 18.49:
    print("Baixo peso Grau I")
elif imc == 18.50 or imc < 24.99:
    print("Peso ideal")
elif imc == 25 or imc < 29.99:
    print("Sobrepeso")
elif imc == 30 or imc < 34.99:
    print("Obesidade Grau I")
elif imc == 35 or imc < 39.99:
    print("Obesidade Grau II")
elif imc >= 40:
    print("Obesidade Grau III")


