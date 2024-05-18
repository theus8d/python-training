# Faça um Programa que converta metros para centímetros.
while True:
    metro=input("Digite a quantidade de metros em valor numérico: ")
    if metro.isnumeric():
        break
    print("Não é permitido o uso de letras ")
print("O valor convertido em centímetros foi: ", int(metro)*100)