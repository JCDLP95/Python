import random

choices = ["Rock", "Paper", "Scissors"]

player1_score = 0
player2_score = 0

while True:
    player1 = input("Jugador 1, Escoge entre Rock, Paper o Scissors: ").lower()

    opcion = random.choice(choices).lower()

    print(f"Jugador 2 (computadora) elige: {opcion}")

    if (player1 == "rock" and opcion == "scissors") or (player1 == "paper" and opcion == "rock") or (player1 == "scissors" and opcion == "paper"):
        print("Jugador 1 gana!")
        player1_score += 1
    elif player1 == opcion:
        print("Tenemos un empate!")
    else:
        print("Jugador 2 gana!")
        player2_score += 1

    if player1_score == 2 or player2_score == 2:
        if player1_score > player2_score:
            print("¡Jugador 1 ha ganado el juego!")
        else:
            print("¡Jugador 2 ha ganado el juego!")
        print("¡Gracias por jugar!")
        break
