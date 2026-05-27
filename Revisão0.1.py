print("Hello, World!")

nome_usuario = "Allyson"      # str
idade = 18                    # int
altura = 1.75                 # float
programador = True            # bool


print("Nome:", nome_usuario, "-> Tipo:", type(nome_usuario))
print("Idade:", idade, "-> Tipo:", type(idade))

# Uma forma moderna de juntar texto e variáveis: f-strings
print(f"Olá! Meu nome é {nome_usuario} e eu tenho {idade} anos.")


#atividade de cadastro

print("cadastro de usuário")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ycidade = input("Digite a cidade em que você reside: ")

print(f"Oi, {nome}! Você tem {idade} anos e mora numa das cidades mais lindas do mundo, {ycidade}, que é conhecida por sua capital perigosa.")

