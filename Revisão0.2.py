infantil = 15.00
Adulto = 30.00
idoso = 20.00
idade = int(input("Digite sua idade: "))
if idade < 12: 
    print("Você se enquadra na categoria infantil. ")
    print(f"Valor do ingresso: R$ {infantil}")
elif idade >=12 and idade < 60:
    print("Você se enquadra na categoria adulto. ")
    print(f"Valor do ingresso: R$ {Adulto}")
else:  
    print("Você se enquadra na categoria idoso. ")
    print(f"Valor do ingresso: R$ {idoso}")
   