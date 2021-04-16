import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

# nave
naveImg = pygame.image.load('imagens/nave.png')
naveX = 50
naveY = 500

# tela de fundo
fundoImg = pygame.image.load('imagens/fundo.jpg')

# asteroides
asteroideImg = pygame.image.load('imagens/asteroide.png')
asteroideX = 200
asteroidey = 150

def nave():
    screen.blit(naveImg, (naveX, naveY))

def asteroide():
    screen.blit(asteroideImg, (asteroideX, asteroidey))

running = True
while running:

    screen.fill((0,0,0,))
    screen.blit(fundoImg, (0,0))
    nave()
    asteroide()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


    pygame.display.update()
