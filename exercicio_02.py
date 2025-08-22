# Solicita o peso e a altura do usuário
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

imc = peso / (altura ** 2)

if imc<18.5:
    print("Abaixo do peso")

elif imc<=18.5 or imc<25:
    print("peso normal")

elif imc<=25 or imc<30:
    print("sobrepeso")

else:
    print("Obesidade")













