# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
while True:
    nota=input("Digite a primeira nota: ")
    nota_2=input("Digite a segunda nota: ")
    nota_3=input("Digite a terceira nota: ")
    nota_4=input("Digite a quarta nota nota: ")
    if nota.isnumeric() and nota_2.isnumeric() and nota_3.isnumeric() and nota_4.isnumeric():
        break
    print("Não é permitido o uso de letras ")
print("A sua média bimestral foi: ", (int(nota) + int(nota_2) +int(nota_3) + int(nota_4)) /4)