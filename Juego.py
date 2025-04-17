import os
import time
import random

print("Welcome to Dungeons and Dragons")
time.sleep(1)
os.system("clear")

while True:
    username = input("Choose the name of your character: ")
    character_type = input("Choose your character type: ")

    print(f"Welcome {username} the {character_type} to the adventure!") 
    time.sleep(3)
    os.system("clear")

    print("Let's create your health stats")
    healthStat = random.randint(1, 10) + 12

    print("Let's create your strength stats")
    strengthStat = random.randint(1, 10) + 12

    print(f"Your user has {healthStat} health and {strengthStat} strength.")

    again = input("Would you like to create another character? Yes or No: ")
    if again.lower() == "yes":
        print("Let's go again!")
        time.sleep(1)
        os.system("clear")
    elif again.lower() == "no":
        print("Thank you for playing!")
        break
    else:
        print("Wrong answer spelled. Try again.")
        time.sleep(1)
        os.system("clear")
