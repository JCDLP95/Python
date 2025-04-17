import os
import time

print("Welcome to iTunes")
time.sleep(1)
os.system("clear")

while True:
    username = input("Choose 0 to play a song or 1 to exit: ")

    if username == "0":
        print("AC/DC, TNT")
        break
    elif username == "1":
        print("Off")
        break
    else:
        print("Wrong button. Try again.")
        time.sleep(1)
        os.system("clear")
