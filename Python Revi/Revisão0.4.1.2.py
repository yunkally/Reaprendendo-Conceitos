#Calculadora de imc

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)
print(f"{nome}, seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com peso normal.")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade. Consulte um profissional de saúde para orientação.")