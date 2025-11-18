#Faça um programa em python que abra e reproduza o aúdio de um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load('gripadinha.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait(1)
pygame.mixer.music.stop()