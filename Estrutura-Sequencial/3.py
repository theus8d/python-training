# Faça um Programa que peça dois números e imprima a soma.
while True:
    numero=input( "Digite o numero que deseja fazer a soma: " )
    numero_2=input("Digite o segundo numero da soma: ")
    if numero.isnumeric() and numero_2.isnumeric():
        break
    print ("Não é permitido a soma de letras ")
print ( "O resultado da sua soma foi:", (int(numero) + int(numero_2)))