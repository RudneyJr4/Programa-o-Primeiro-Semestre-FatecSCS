import math

a= b = c = delta = x1 = x2 = 0.00

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
	print("Essa equação não é quadrática, impossível de continuar.")
else:
	delta = (b ** 2) - (4 * a * c)
	if delta < 0:
		print("Essa equação não possui raízes reais.")
	elif delta == 0:
		x1 = (-b + math.sqrt(delta)) / (2 * a)
		print(f"Essa equação possui apenas uma raiz real: {x1:.2f}")
	else:
		x1 = (-b + math.sqrt(delta)) / (2 * a)
		x2 = (-b - math.sqrt(delta)) / (2 * a)
		print(f"Essa equação possui duas raízes reais: {x1:.2f} e {x2:.2f}")