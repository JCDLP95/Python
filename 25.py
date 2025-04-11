import random

def password(length):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contraseña = ""
    for _ in range(length):
        contraseña += random.choice(caracteres)
    return contraseña

user = password(10)
print(user)