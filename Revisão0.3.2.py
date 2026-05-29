#Calculadora de operações básicas de matemática

funcao = input("Digite a operação que deseja realizar (soma, subtração, multiplicação, divisão): ")
number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))
if funcao.lower() == "soma":
    resultado = number1 + number2
    print(f"O resultado da soma é: {resultado}")
elif funcao.lower() == "subtração":
    resultado = number1 - number2
    print(f"O resultado da subtração é: {resultado}")
elif funcao.lower() == "multiplicação":
    resultado = number1 * number2
    print(f"O resultado da multiplicação é: {resultado}")
elif funcao.lower() == "divisão":
    if number2 != 0:
        resultado = number1 / number2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida. ")
else:
    print("Operação inválida. Por favor, escolha entre soma, subtração, multiplicação ou divisão.")
