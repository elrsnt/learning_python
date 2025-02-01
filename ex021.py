# Faca um programa em python que abra e reproduza um audio de um arquivo mp3
import pygame
paygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
