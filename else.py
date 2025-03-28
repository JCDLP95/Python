print ("Juguemos piedra, papel o tijera")
print ("Se juega al primero en llegar a 2 puntos")

player1 = 0
player2 = 0

while True :
  player1 = input("Jugador 1, elige piedra, papel o tijera: ")
  player2 = input("Jugador 2, elige piedra, papel o tijera:")

  if (player1 == "piedra" and player2 == "tijera") or (player1 == "papel" and player2 == "piedra") or (player1 == "tijera" and player2 == "papel"):
    print ("Jugador 1 gana") 
    player1 += 1
  elif player1 == player2:
   print ("Empate")
else:
  print ("Jugador 2 gana")
  player2 += 1

if player1==2 or player2==2:
  print("Thanks for playing!")
  exit()
