
nome = input("Digite seu nome: ")
print(f"Olá {nome}, seja bem vindo(a)!")   
idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Você é menor de idade!") 
else:
    print("Você é maior de idade!") 

print("Vamos fazer uma conta de divisão!")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
divisao = n1 / n2
print(f"A divisão entre {n1} e {n2} é igual a {divisao}")


print("Obrigado por usar nosso sistema, volte sempre!") 
print("Fim do programa!")