#mostra a tábuada de um número

#Variáveis
tabuada = resultado = contador = 0.0

tabuada = int(input ("Qual a tabuada a exibir?"))

contador = 1
while(contador <= 10):
    resultado = tabuada * contador
    print(f"{tabuada} x {contador} = {resultado}")

    #incrementa
    contador = contador + 1