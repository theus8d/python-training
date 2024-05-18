# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# O produto do dobro do primeiro com metade do segundo .
# A soma do triplo do primeiro com o terceiro
# o terceiro elevado ao cubo.
while True:
    numero=input("Digite o primeiro numero: ")
    numero_2=input("Digite o segundo numero: ")
    numero_3=input("Digite o terceiro numero: ")
    if numero.replace(".","").isnumeric() and numero_2.replace(".","").isnumeric() and numero_3.replace(".","").isnumeric():
        break
    print("Não é permitido o uso de letras ")
resultado= float(numero)*2 * float(numero_2)/2
print("A :", resultado )
resultado_2=float(numero)*3 + float(numero_3)
print("B:", resultado_2)
resultado_3=pow(float(numero_3), 3)
print("C:", resultado_3)