# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
while True:
    fah=input("Digite a temperatura em Fahrenheit: ")
    if fah.isnumeric():
        break
    print("Não é permitido o uso de letras ")
cel=5*((int(fah)-32)/9)
print("A sua temperatura transformada em Celsius foi: ", cel)