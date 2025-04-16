import os
import time

print("Welcome to iTunes")
time.sleep(1)
os.system("clear")

username = input("Choose 0 to play a song or 1 to exit: ")

if username == "0":
    print("AC/DC, TNT")
elif username == "1":
    print("Off")
else:
    print("Wrong button")
