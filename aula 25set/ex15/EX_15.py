salario = salarioNovo = 0.0

#entrada de dados
salario = float(input("Digite o valor do seu Salário: "))

salarioNovo = salario
#calculos
#if (salario < 2000) :
# salarioNovo = salario * 0.10
#else :
# salarioNovo = salario

if(salario < 2000) :
    salarioNovo = salario * 1.10

#Saida
print(f"Seu salário antigo é R$ {salario:10.2f}")
print(f"Seu salário atualizado é R$ {salarioNovo:10.2f}")
