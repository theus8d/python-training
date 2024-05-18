# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
while True:
    cel=input("Digite a temperatura em Celsius: ")
    if cel.isnumeric():
        break
    print("Não é permitido o uso de letras ")
fah=((int(cel)*1.8)+32)
print("A sua temperatura transformada em  Fahrenheit foi: ", fah)