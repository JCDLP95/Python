import random

def dado(giro1, giro2, giro3):
    
    giro1 = random.randint(1, 6)
    giro2 = random.randint(1, 6)
    giro3 = random.randint(1, 6)

    print(f"Giro 1: {giro1}")
    print(f"Giro 2: {giro2}")
    print(f"Giro 3: {giro3}")


dado(0, 0, 0)
