
print("Youtube STUDIO FIAP","\nPlanos Disponiveis:")

print("* basic","\n* silver","\n* gold","\n* platinum\n")


plano = input("Qual seu plano de assinatura? ")
valor = float(input("Valor do seu faturamento anual: R$"))

if plano == "basic":
    valor = valor * 0.3
    print("O valor do bonus é R$",valor)
elif plano == "silver":
    valor = valor * 0.2
    print("O valor do bonus é R$",valor)
elif plano == "gold":
    valor = valor * 0.1
    print("O valor do bonus é R$",valor)
elif plano == "platinum":
    valor = valor * 0.05
    print("O valor do bonus é R$",valor)
else:
    print("Você não inseriu um plano de assinatura valido!")
