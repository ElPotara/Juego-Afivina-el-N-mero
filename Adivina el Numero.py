# adivina_el_numero.py

import random

def jugar_adivina_el_numero():
    """
    Juego interactivo donde el usuario debe adivinar un número aleatorio.
    """
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinanza = 0

    print("¡Bienvenido a 'Adivina el Número'!")
    print("He pensado en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while adivinanza != numero_secreto:
        try:
            adivinanza = int(input("\nIngresa tu número: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("¡Muy bajo! Intenta con un número más grande.")
            elif adivinanza > numero_secreto:
                print("¡Muy alto! Intenta con un número más pequeño.")
            else:
                print(f"\n¡Felicidades! Adivinaste el número en {intentos} intentos.")
                print(f"El número secreto era {numero_secreto}.")

        except ValueError:
            print("Error: Por favor, ingresa solo números enteros.")

if __name__ == "__main__":
    jugar_adivina_el_numero()