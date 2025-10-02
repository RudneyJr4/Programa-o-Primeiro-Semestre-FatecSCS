l1 = l2 = l3 = 0.0
l1 = float(input("Digite o valor do lado 1: "))
l2 = float(input("Digite o valor do lado 2: "))
l3 = float(input("Digite o valor do lado 3: "))

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    if (l1 == l2) and (l2 == l3):
        print("É um Triângulo equilátero")
    elif (l1 == l2 != l3) or (l1 == l3 != l2) or (l2 == l3 != l1):
        print("É um Triângulo isósceles")
    else:
        print("É um Triângulo escaleno")
else: print("Não é um Triângulo")
