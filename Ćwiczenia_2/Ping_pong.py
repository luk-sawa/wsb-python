import sys
import pygame
from pygame.locals import *
import random
pygame.init()
FPS = 30
fpsZegar = pygame.time.Clock()
OKNOGRY_SZER = 800
OKNOGRY_WYS = 500
OKNOGRY = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)
pygame.display.set_caption('Prosty Pong')
LT_BLUE = (230, 255, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (192, 192, 192)
VIOLET = (120, 0, 120)
ORANGE = (255, 128, 0)
BALL_COLORS = (RED, GREEN, BLUE)

# rozmiar paletek
PALETKA_SZER = 20
PALETKA_WYS = 80

# wygląd i pozycja początkowa paletki 1
PALETKA_1_POZ = (30, 200)
paletka1_obr = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka1_obr.fill(ORANGE)
paletka1_prost = paletka1_obr.get_rect()
paletka1_prost.x = PALETKA_1_POZ[0]
paletka1_prost.y = PALETKA_1_POZ[1]

# wygląd i pozycja początkowa paletki 2
PALETKA_2_POZ = (750, 200)
paletka2_obr = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka2_obr.fill(VIOLET)
paletka2_prost = paletka2_obr.get_rect()
paletka2_prost.x = PALETKA_2_POZ[0]
paletka2_prost.y = PALETKA_2_POZ[1]

# wygląd paletki 3
PALETKA_3_POZ = (390, -100)
paletka3_obr = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka3_obr.fill(GREY)
paletka3_prost = paletka3_obr.get_rect()
paletka3_prost.x = PALETKA_3_POZ[0]
paletka3_prost.y = PALETKA_3_POZ[1]
paletka3_direction = 1

# szybkość wrogiej paletki
AI_PREDKOSC = 7

# wygląd i rozmiar piłeczki
PILKA_SZER = 20
PILKA_WYS = 20
PILKA_PREDKOSC_X = 6
PILKA_PREDKOSC_Y = 6
pilka_obr = pygame.Surface([PILKA_SZER, PILKA_WYS], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(pilka_obr, GREEN, [0, 0, PILKA_SZER, PILKA_WYS])
pilka_prost = pilka_obr.get_rect()
pilka_prost.x = OKNOGRY_SZER/2
pilka_prost.y = OKNOGRY_WYS/2

# ustawienia początkowe
GRACZ_1_PKT = '0'
GRACZ_2_PKT = '0'
fontObj = pygame.font.Font('pingpong.ttf', 64)


# funkcja wyświetlania wyniku gracza1
def drukuj_punkty_p1():
    tekst_obr1 = fontObj.render(GRACZ_1_PKT, True, (0, 0, 0))
    tekst_prost1 = tekst_obr1.get_rect()
    tekst_prost1.center = (OKNOGRY_SZER * 0.15, OKNOGRY_WYS / 2)
    OKNOGRY.blit(tekst_obr1, tekst_prost1)


# funkcja wyświetlania wyniku gracza2
def drukuj_punkty_p2():
    tekst_obr2 = fontObj.render(GRACZ_2_PKT, True, (0, 0, 0))
    tekst_prost2 = tekst_obr2.get_rect()
    tekst_prost2.center = (OKNOGRY_SZER * 0.85, OKNOGRY_WYS / 2)
    OKNOGRY.blit(tekst_obr2, tekst_prost2)


while True:
    for event in pygame.event.get():
        # wyjście:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # poruszanie paletką:
        if event.type == MOUSEMOTION:
            myszaX, myszaY = event.pos
            przesuniecie = myszaY-(PALETKA_SZER/2)
            if przesuniecie > OKNOGRY_WYS-PALETKA_WYS:
                przesuniecie = OKNOGRY_WYS-PALETKA_WYS
            if przesuniecie < 0:
                przesuniecie = 0
            paletka1_prost.y = przesuniecie
    # ruch wrogiej paletki
    if pilka_prost.centery > paletka2_prost.centery:
        paletka2_prost.y += AI_PREDKOSC
    elif pilka_prost.centery < paletka2_prost.centery:
        paletka2_prost.y -= AI_PREDKOSC
    # ruch trzeciej paletki
    number = (1, 2, 3, 4, 5, 6)
    if paletka3_prost.top >= OKNOGRY_WYS+20:
        paletka3_direction = -1
    if paletka3_prost.bottom <= 0-20:
        paletka3_direction = 1
    #próba wprowadzenia losowego momentu pojawiania się trzeciej paletki
    #if paletka3_prost.top >= OKNOGRY_WYS and random.choice(number) == 6:
    #    paletka3_direction = -1
    #if paletka3_prost.bottom <= 0 and random.choice(number) == 6:
    #    paletka3_direction = 1
    paletka3_prost.y += AI_PREDKOSC * paletka3_direction
    # ruch piłeczki
    pilka_prost.x += PILKA_PREDKOSC_X
    pilka_prost.y += PILKA_PREDKOSC_Y
    # odbicie piłeczki od ścian
    if pilka_prost.bottom >= OKNOGRY_WYS:
        PILKA_PREDKOSC_Y *= -1
    if pilka_prost.top <= 0:
        PILKA_PREDKOSC_Y *= -1
    # odbicie piłeczki od paletki1
    if pilka_prost.colliderect(paletka1_prost):
        PILKA_PREDKOSC_X *= -1
        pilka_prost.left = paletka1_prost.right
    # odbicie piłeczki od paletki2
    if pilka_prost.colliderect(paletka2_prost):
        PILKA_PREDKOSC_X *= -1
        pilka_prost.right = paletka2_prost.left
    # odbicie piłeczki od paletki3
    if pilka_prost.colliderect(paletka3_prost):
        PILKA_PREDKOSC_X *= -1
        pygame.draw.ellipse(pilka_obr, random.choice(BALL_COLORS), [0, 0, PILKA_SZER, PILKA_WYS])
        if PILKA_PREDKOSC_X < 0:
            pilka_prost.right = paletka3_prost.left
        else:
            pilka_prost.left = paletka3_prost.right
    # wyjście piłeczki po prawej stronie
    if pilka_prost.right >= OKNOGRY_SZER:
        pilka_prost.x = OKNOGRY_SZER/2
        pilka_prost.y = OKNOGRY_WYS/2
        GRACZ_1_PKT = str(int(GRACZ_1_PKT)+1)
    # wyjście piłeczki po lewej stronie
    if pilka_prost.left <= 0:
        pilka_prost.x = OKNOGRY_SZER/2
        pilka_prost.y = OKNOGRY_WYS/2
        GRACZ_2_PKT = str(int(GRACZ_2_PKT)+1)

    # rysowanie obszaru gry
    OKNOGRY.fill(LT_BLUE)
    drukuj_punkty_p1()
    drukuj_punkty_p2()
    OKNOGRY.blit(paletka1_obr, paletka1_prost)
    OKNOGRY.blit(paletka2_obr, paletka2_prost)
    OKNOGRY.blit(paletka3_obr, paletka3_prost)
    OKNOGRY.blit(pilka_obr, pilka_prost)
    pygame.display.update()
    fpsZegar.tick(FPS)