#!/usr/bin/env python

background_image_filename = "mountain.jpg"
stage_one = "super_peter.png"
stage_two = "super_peter_2.png"
stage_three = "super_peter_3.png"
stage_four = "super_peter_god.png"
stage_five = "ssgss_peter.png"
stage_six = "true_peter.png"
stage_special = "FAMILY GUY FUNNY INSTINCT.png"
power_level = 0
width = 1000
height = 600
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

punch_L = pygame.image.load("petah_punch(right).png")
punch_R = pygame.image.load("petah_punch(left).png")
punch_U = pygame.image.load("petah_punch(up).png")
punch_D = pygame.image.load("petah_punch(down).png")
hazard = pygame.image.load("dark_beter.png")
punch_sound = pygame.mixer.Sound("punch.wav")
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("SUPER PETER POWER UP STIMULOAR: THE MOST EPIC OF GAMER ANIME BATTLES!!!!!!?")
background = pygame.image.load(background_image_filename).convert()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    if power_level > 100 and power_level <= 200:
        mouse_cursor = pygame.image.load(stage_two).convert_alpha()
    elif power_level > 200 and power_level <= 300:
        mouse_cursor = pygame.image.load(stage_three).convert_alpha()
    elif power_level > 300 and power_level <= 400:
        mouse_cursor = pygame.image.load(stage_four).convert_alpha()
    elif power_level > 400 and power_level <= 500:
        mouse_cursor = pygame.image.load(stage_five).convert_alpha()
    elif power_level > 500 and power_level <= 9000:
        mouse_cursor = pygame.image.load(stage_six).convert_alpha()
    elif power_level > 9000:
        mouse_cursor = pygame.image.load(stage_special).convert_alpha()
    else:
        mouse_cursor = pygame.image.load(stage_one).convert_alpha()

    screen.blit(background, (0,0))

    x, y = pygame.mouse.get_pos()
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    screen.blit(mouse_cursor, (x, y))
    screen.blit(hazard,(700, 150))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print(power_level)
            power_level += 0.25
        if event.key == pygame.K_LEFT:
                pygame.mixer.Sound.play(punch_sound)
                screen.blit(punch_L, (x - 200, y + 15))
                pygame.mixer.music.stop()
        elif event.key == pygame.K_RIGHT:
                pygame.mixer.Sound.play(punch_sound)
                screen.blit(punch_R, (x + 200, y + 15))
                pygame.mixer.music.stop()
        elif event.key == pygame.K_UP:
                pygame.mixer.Sound.play(punch_sound)
                screen.blit(punch_U, (x, y - 150))
                pygame.mixer.music.stop()
        elif event.key == pygame.K_DOWN:
                pygame.mixer.Sound.play(punch_sound)
                screen.blit(punch_D, (x, y + 180))
                pygame.mixer.music.stop()
        elif event.key == pygame.K_DOWN and pygame.K_UP and pygame.K_LEFT:
                pygame.mixer.Sound.play(punch_sound)
                screen.blit(punch_L, (x - 200, y - 150))
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(punch_sound)
                screen.blit(punch_L, (x - 200, y + 15))
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(punch_sound)
                screen.blit(punch_L, (x - 200, y + 150))
                pygame.mixer.music.stop()

    pygame.display.update()
