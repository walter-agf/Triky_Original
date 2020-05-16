# -*- coding: utf-8 -*-
"""
@author: Jackh & Alejandro 
"""
import random
def dibujarTablero(tablero):
    # arreglo/lista de 10 posiciones, se ignora la primera posición
    print(" " + tablero[7] + " | " + tablero[8] + " | " + tablero[9],"                 7 | 8 | 9 ")
    print("-----------                -----------") 
    print(" " + tablero[4] + " | " + tablero[5] + " | " + tablero[6],"                 4 | 5 | 6 ")
    print("-----------                -----------")
    print(" " + tablero[1] + " | " + tablero[2] + " | " + tablero[3],"                 1 | 2 | 3 ")
def inputUsuarioLLeva():# Usuario elige que desea llevar, devuelve una lista, el primero es lo que llevará el usuario
    lleva = ""
    while not (lleva == "X" or lleva == "O"):
        print("Quieres llevar X ó O?")
        lleva = input("-------> ").upper()
    if lleva == "X":
        return ["X","O"]
    else:
        return ["O","X"]
def QuienJuegaPrimero():
    # elije al azar el jugador que va primero
    if random.randint(0, 1) == 0:
        return "Computadora"
    else:
        return "Usuario"
def jugarNuevamente():#Volver a jugar? si dice no, es false
    print("\nQuieres jugar de nuevo? (si o no)")
    return input().lower().startswith("s")
def HacerMovimiento(tablero, lleva, mover):
    tablero[mover] = lleva
def ganador(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Arriba
    (bo[4] == le and bo[5] == le and bo[6] == le) or # Medio
    (bo[1] == le and bo[2] == le and bo[3] == le) or # Abajo
    (bo[7] == le and bo[4] == le and bo[1] == le) or # Izquierda
    (bo[8] == le and bo[5] == le and bo[2] == le) or # Media
    (bo[9] == le and bo[6] == le and bo[3] == le) or # Derecha
    (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal
def copiaTablero(tablero):# Duplicado del tablero
    dupeTablero = []
    for i in tablero:
        dupeTablero.append(i)
    return dupeTablero
def espacioLibre(tablero, mover):# True si el movimiento es valido
    return tablero[mover] == " "
def movimientoUsuario(tablero):# el usuario elije movimiento
    mover = " "
    while mover not in "1 2 3 4 5 6 7 8 9".split() or not espacioLibre(tablero, int(mover)):
        print("\nCual es tu siguiente movimiento? (1-9)")
        mover = input()
    return int(mover)
def movimientoAletarioLista(tablero, movimientoLista):# Devuelve movimiento valido, None si es movimiento es invalido
    movimientosPosibles = []
    for i in movimientoLista:
        if espacioLibre(tablero, i):
            movimientosPosibles.append(i)
    if len(movimientosPosibles) != 0:
        return random.choice(movimientosPosibles)
    else:
        return None
def movimientoComputadora(tablero, computadoraLleva):#Donde moverse, computadora
    if computadoraLleva == 'X':
        usuarioLleva = 'O'
    else:
        usuarioLleva = 'X'
    #Se puede ganar en el proximo movimiento?
    for i in range(1, 10):
        copia = copiaTablero(tablero)
        if espacioLibre(copia, i):
            HacerMovimiento(copia, computadoraLleva, i)
            if ganador(copia, computadoraLleva):
                return i
    #Si el usuario puede ganar, bloquea esa casilla
    for i in range(1, 10):
        copia = copiaTablero(tablero)
        if espacioLibre(copia, i):
            HacerMovimiento(copia, usuarioLleva, i)
            if ganador(copia, usuarioLleva):
                return i
    #Tomar esquinas
    mover = movimientoAletarioLista(tablero, [1, 3, 7, 9])
    if mover != None:
        return mover
    #Tomar centro
    if espacioLibre(tablero, 5):
        return 5
    #Tomar lado
    return movimientoAletarioLista(tablero, [2, 4, 6, 8])
def tableroLleno(tablero):#Devuelve true si se ocuparon los espacio, Devuelve False si no.
    for i in range(1, 10):
        if espacioLibre(tablero, i):
            return False
    return True