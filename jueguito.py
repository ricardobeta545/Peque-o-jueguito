import random

palabras = ["python", "capibara", "terror", "videojuego"]

palabra = random.choice(palabras)
letras_adivinadas = []
vidas = 6

while vidas > 0:
    progreso = ""

    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "

    print("\nPalabra:", progreso)

    if "_" not in progreso:
        print(" Ganaste")
        break

    intento = input("Ingresa una letra: ").lower()

    if intento in palabra:
        letras_adivinadas.append(intento)
        print("Correcto")
    else:
        vidas -= 1
        print(" Incorrecto")
        print("Vidas:", vidas)

if vidas == 0:
    print(" Perdiste")
    print("La palabra era:", palabra)