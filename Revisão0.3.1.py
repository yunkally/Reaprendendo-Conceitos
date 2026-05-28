#Contador de round valorant

teamname = input("Digite o nome do seu time: ")

for round in range (1, 25):
    print(f"Round {round} - {teamname}")
    if round == 3:
        print("Round armado! Dinheiro extra para o time!")
        roundwin = input("Vocês ganharam o round armado? (S/N) ")
        if roundwin.upper() == "S":
            print("Parabéns! Vocês ganharam o round armado!")
        else:           print("Que pena! Vocês perderam o round armado.foque no farm")
    if round == 12:
        roundwin = input("Vocês ganharam o round 11? (S/N) " )
        if roundwin.upper() == "S":
            print("Parabéns! falta só 1 round para a vitória!")
        else:          print("Que pena! Vocês perderam o round 11. Foquem no farm e na economia para o próximo round!")
    

