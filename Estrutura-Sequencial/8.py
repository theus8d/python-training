# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
while True:
    valor=input("Digite qual o valor recebido por hora: ")
    hora=input("Digite a quantidade horas trabalhada ")
    if valor.isnumeric() and hora.isnumeric():
        break
    print("Não é permitido o uso de letras ")
total=int(valor)*int(hora)
print("O valor recebido mensalmente é :",total)