print("Bienvenido al quiz")
print()
print("Dime un número y te daré 10 problemas")
print()

problema = int(input("Escoge tu número:"))
contador = 0

for i in range(1, 11):
    respuesta = problema * i
    print(i, "x", problema)
    respuesta_usuario = int(input("> "))
    if respuesta_usuario == respuesta:
        print("¡Lo acertaste!")
        contador += 1
    else:
        print("Eso no es correcto. Debería haber sido", respuesta)

print("Has acertado", contador, "de 10 preguntas.")
