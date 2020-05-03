import sys, pygame

#Inicializamos pygame
pygame.init()
#Hacemos la ventana
width, height = 1000, 600
canva = width, height
screen = pygame.display.set_mode(canva)
#Desplegamos el nombre del juego
pygame.display.set_caption("Juego BALL")
#Declaramos e inicializamos variables
#width, height = 800, 600
speed = [1, 1]
white = 255, 255, 255
#Crear objeto pelota
ball = pygame.image.load("ball2.jpg")
ballrect = ball.get_rect()
#Crear objeto bate
bate = pygame.image.load("barra-lateral-roja2.png")
baterect = bate.get_rect() 
#Poner el bate en el medio de la pantalla
baterect.move_ip(950, 300)

#Comenzamos bucle del juego
run = True
while run:
  #Retrazo de la pelota
    pygame.time.delay(1)
  #Captura de eventos producidos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
#Movimiento con las teclas
keys = pygame.key.get_pressed()
if keys[pygame.K_UP]:
  baterect = baterect.move(0, -1)
if keys[pygame.K_DOWN]:
  baterect = baterect.move(0, 1)
#Compruebo la colisión
if baterect.colliderect(ballrect):
  speed[0] = -speed[0]
#Muevo la pelota
ballrect = ballrect.move(speed)
#Compruebo que la pelota llega a los lìmites de la ventana
if ballrect.left < - 25 or ballrect.right > width + 25:
    speed[0] = -speed[0]
if ballrect.top < - 25 or ballrect.bottom > height + 25:
    speed[1] = -speed[1]
#Hacer fondo blanco y dibujar la pelota y se actualiza la pantalla
screen.fill(white)
screen.blit(ball, ballrect)
#Dibujando el bate
screen.blit(bate, baterect)
pygame.display.flip()
#Salir del juego
pygame.quit()