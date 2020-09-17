minuto = int(input("Insira o minuto atual: "))
fatorial = 1
while minuto > 0:
    fatorial = fatorial * minuto
    minuto = minuto -1
print("A senha do servidor é 'LIBERDADE{}'".format(fatorial))
