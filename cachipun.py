import sys

import random

opciones = ["piedra","papel","tijeras"]

while True:
    jugador = input("elige: piedra, papel o tijeras o escribe 'salir'")

    if jugador == "salir":
        print("! juego terminado")
        break

    if jugador not in opciones:
        print(" opcion no valida...")
        continue

    computador = random.choices(opciones)

    print(f"el jugador eligio : {jugador} y el computador eligio : {computador[0]}")

    computador = computador[0]
    if jugador == computador:
        print("empate!!..")

    elif (jugador == "piedra" and computador == "tijeras") or\
         (jugador == "papel" and computador == "piedra") or\
         (jugador == "tijeras" and computador == "papel"):
         print("ganaste!!")
    else:
        print("perdiste!!!")