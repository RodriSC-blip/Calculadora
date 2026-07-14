valor = int(input("Digite um valor: "))

for valor in range(valor + 1):
    print(" ")
    print( "TABUADA DA ABELINHA:")

    for i in range(1, 11):
        print(f"{valor} x {i} = {valor*i}")

print(" ")
