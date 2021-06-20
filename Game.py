import pygame

pygame.init()

screen = pygame.display.set_mode((900, 600))

pygame.display.set_caption("Internalium")
icon = pygame.image.load('Gambar.jpg')
pygame.display.set_icon(icon)


screen.fill("#ffffff")

image = pygame.image.load('Roket.jpg')
image1 = 43
image2 = 282
image1_change = 0

roket = pygame.image.load("Roket.jpg")
roket1 = 489
roket2 = 282
roket1_change = 1

c = [0.1, 0.2, 0.3, 0.4, 0.5]

import random

a = random.choice(c)
b = random.choice(c)

def Roket(f, a):
    screen.blit(roket, (f, a))

def main(x, y):
    screen.blit(image, (x, y))

running = True

while running:

    image2 -= b
    roket2 -= a


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    main(image1, image2)
    Roket(roket1, roket2)
    pygame.display.update()
