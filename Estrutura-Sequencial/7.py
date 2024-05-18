# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
while True:
    lado=input("Digite o valor referente a um dos lados do quadrado: ")
    if lado.isnumeric():
        break
    print("Não é permitido o uso de letras ")
area=(int(lado)*int(lado))
print("O resultado foi:", area*2)