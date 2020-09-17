# Esse programa pega o valor digitado pelo usuario e eleva ao 3^, o resultado é guardado e exibido em uma outra lista.

lista_a = []
lista_b = []

for i in range(8):
    lista_a.append (int(input("Digite um numero inteiro:")))
    lista_b.append (lista_a[i] ** 3)

    print(lista_b)
    
