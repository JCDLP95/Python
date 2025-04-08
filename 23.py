def signIn():
 while True:
    nombre = input("¿Cuál es tu nombre?: ")
    if nombre == "Juan" or "juan":
        passw = input("Ingresa tu contraseña: ")
        if passw == "1234":
            print("Bienvenido Juan")
            break
        else:
            print("Contraseña incorrecta")
    else:
        print("No estás registrado")


signIn()