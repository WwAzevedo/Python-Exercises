print("**********Resultado para cronograma de transmissão**********")

segunda = int(input("Número de votos na Segunda-Feira: "))
terca = int(input("Número de votos na Terça-Feira: "))
quarta = int(input("Número de votos na Quarta-Feira: "))
quinta = int(input("Número de votos na Quinta-Feira: "))
sexta = int(input("Número de votos na Sexta-Feira: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("Segunda-Feira é eleito o melhor dia para transmissões!")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("Terça-Feira é eleito o melhor dia para transmissões")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("Quarta-Feira é eleito o melhor dia para transmissões")
elif quinta > segunda and quinta > quarta and quinta > terca and quinta > sexta:
    print("Quinta-Feira é eleito o melhor dia para transmissões")
elif sexta > segunda and sexta > quarta and sexta > quinta and sexta > terca:
    print("Sexta-Feira é eleito o melhor dia para transmissões")
elif segunda == 0 and quarta == 0 and quinta == 0 and sexta == 0:
    print("Não houve votos em nenhum dia da semana!")
else:
    print("Houve um empate em todos os dias da semana!")
