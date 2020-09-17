
print("***************CALCULO DE CALORIAS - HealthTrack***************\n")
i = input("Deseja inserir um novo alimento? Responda (sim) ou (não): ")
soma = 0

while i == "sim":

      
    a = input("Insira o alimento que você consumiu:\n")
    c = int(input("Quantas calorias possui?\n"))
    p = int(input("Quantas porçoes?\n"))
    
    resultado = c * p
    soma = soma + resultado

    print("--------------------------------------------------------------------------")
    print("Alimento cadastrado com sucesso! \n{} {}(s) com total de {} calorias".format(p,a,resultado))
    print("*****Você consumiu um total de {} calorias hoje*****".format(soma))
    print("--------------------------------------------------------------------------")
    
    i = input("Deseja inserir um novo alimento? Responda (sim) ou (não):\n")


print("--------------------------------------------------------")
print("*****Você consumiu um total de {} calorias hoje*****".format(soma))
print("--------------------------------------------------------") 
