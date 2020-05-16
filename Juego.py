# -*- coding: utf-8 -*-
"""
@author: Jackh & Alejandro 
"""
from Funciones import inputUsuarioLLeva,QuienJuegaPrimero,dibujarTablero,movimientoUsuario,HacerMovimiento,ganador,tableroLleno,movimientoComputadora,jugarNuevamente
x = open("intro.txt","r")
g = x.read()
print (g)
x.close()
while True:# Reiniciar tablero
    ElTablero = [' '] * 10
    usuarioLleva, computadoraLleva = inputUsuarioLLeva()
    turn = QuienJuegaPrimero()
    print("\nEl Jugador [ ",turn," ] va primero")
    juegoOn = True
    while juegoOn:
        if turn == "Usuario":
            print("\n ----- Es tu turno ----- \n")#Turno de el usuario
            dibujarTablero(ElTablero)
            mover = movimientoUsuario(ElTablero)
            HacerMovimiento(ElTablero, usuarioLleva, mover)
            if ganador(ElTablero, usuarioLleva):
                dibujarTablero(ElTablero)
                print("\nExcelente! Ganaste el juego!")
                juegoOn = False
            else:
                if tableroLleno(ElTablero):
                    dibujarTablero(ElTablero)
                    print("\nEmpate!")
                    break
                else:
                    turn = "Computadora"
        else:#Turno de la computadora
            mover = movimientoComputadora(ElTablero, computadoraLleva)
            HacerMovimiento(ElTablero, computadoraLleva, mover)
 
            if ganador(ElTablero, computadoraLleva):
                dibujarTablero(ElTablero)
                print("\nPerdiste, la computadora ganó.")
                juegoOn = False
            else:
                if tableroLleno(ElTablero):
                    dibujarTablero(ElTablero)
                    print("\nEmpate!")
                    break
                else:
                    turn = "Usuario"
    if not jugarNuevamente():
        break