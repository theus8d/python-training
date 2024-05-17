# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
while True:
    numero=input("Digite um numero de sua escolha ")
    if numero.isnumeric():
        break
    print(" Não é permitido inserir letras ")
        
print( "O numero informado foi: ", numero)