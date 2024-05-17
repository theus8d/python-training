# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
while True:
    bola=input("Digite o raio correspondente ao circulo: ")
    if bola.isnumeric():
        break
    print("Não é permitido o uso de letras ")
area=(int(bola)*int(bola))*3.1415
print("O resultado foi:", area)