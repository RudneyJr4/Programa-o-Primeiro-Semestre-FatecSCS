# 23)	(IF/OPERADOR LÓGICO) Solicitar do usuário uma determinada idade de um nadador. Baseado nesta idade indique qual a categoria ao qual ele pertente:
# •	Sem Categoria  menor que 5 anos;
# •	Infantil A 5 – 7 anos;
# •	Infantil B 8 – 10 anos;
# •	Juvenil A 11 – 13 anos;
# •	Juvenil B 14 – 17 anos;
# •	Adulto 18 – 60 anos;
# •	Senior Acima de 60 anos
# Resolva esse problema de duas maneiras, uma utilizando exclusivamente SE´s encadeados e outra usando SE simples

idade = int(input("Digite a Idade: "))

#usando IF simples COM operador Lógico
if(idade < 5):
    print("Sem Categoria")
    
if(idade >= 5 and idade <= 7):
    print("Infantil A")
    
if(idade >= 8 and idade <= 10):
    print("Infantil B")
    
if(idade >= 11 and idade <= 13):
    print("Juvenil A")
    
if(idade >= 14 and idade <= 17):
    print("Juvenil B")
    
if(idade >= 18 and idade <= 60):
    print("Adulto")                

if(idade > 60):
    print("Senior")    
    
#usando IF Encadeado SEM operador Lógico
#bem melhor estruturado
if(idade < 5):
    print("Sem Categoria")
elif(idade <= 7):
    print("Infantil A")
elif(idade <= 10):
    print("Infantil B")
elif(idade <= 13):
    print("Juvenil A")
elif(idade <= 17):
    print("Juvenil B")
elif(idade <= 60):
    print("Adulto")                
else:
    print("Senior")   