#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
#import playsound   
import pygame
# Inicializando o mixer PyGame
#playsound.playsound('D:\GoogleDrive\Python\Projeto\Exercicios\ex021.mp3')
pygame.mixer.init()
# Iniciando o Pygame
#pygame.init()
pygame.mixer.music.load('D:\GoogleDrive\Python\Projeto\Exercicios\ex021_Alarm_Clock.mp3')
pygame.mixer.music.play()
x = input('digite algo para encerrar ...')
#pygame.event.wait()