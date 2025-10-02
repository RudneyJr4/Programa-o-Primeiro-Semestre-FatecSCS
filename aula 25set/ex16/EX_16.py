salBruto = salLiquido = inss = irrf = 0.00

#entrada de dados
salBruto = float(input("Qual seu salário bruto? "))

#processamento
if(salBruto < 1500) :
    irrf = 0
    inss = salBruto * 0.08
else :
    irrf = salBruto * 0.05
    inss = salBruto * 0.11

salLiquido = salBruto - irrf - inss

#saida de dados
print(f"Salario Bruto...............: {salBruto:10.2f}")
print(f"INSS........................: {inss:10.2f}")
print(f"IRRF........................: {irrf:10.2f}")
print(f"Salario Liquido.............: {salLiquido:10.2f}")