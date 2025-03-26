from getpass import getpass as input
print("Choose your move R🎸, P📄 or S✄")

player1=(input("Player 1 > "))
player2=(input("Player 2 > "))

if player1 == player2:
  print("It is a draw")
elif player1 == "R" and player2 == "S":
  print("Player 1 wins! Rock beats Scissors")
elif player1 == "S" and player2 == "P":
  print("Player 1 wins! Scissors beats Paper")
elif player1 == "P" and player2 == "R":
  print("Player 1 wins! Paper beats Rock")
elif player2 == "R" and player1 == "S":
  print("Player 2 wins! Rock beats Scissors")
elif player2 == "S" and player1 == "P":
  print("Player 2 wins! Scissors beats Paper")
elif player2 == "P" and player1 == "R":
  print("Player 2 wins! Paper beats Rock")
else:
 print("Invalid input. Please use 'R' for Rock, 'P' for Paper, or 'S' for Scissors.")