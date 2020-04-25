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
#Crear objeto
ball = pygame.image.load("ball.jpg")
ballrect = ball.get_rect()
#Comenzamos bucle del juego
run = True
while run:
  #Retrazo de la pelota
    pygame.time.delay(1)
  #Captura de eventos producidos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
  #Muevo la pelota
    ballrect = ballrect.move(speed)
    #Compruebo que la pelota llega a los lìmites de la ventaa
    if ballrect.left < - 25 or ballrect.right > width + 25:
        speed[0] = -speed[0]
    if ballrect.top < - 25 or ballrect.bottom > height + 25:
        speed[1] = -speed[1]
    #Hacer fondo blanco y dibujar la pelota y se actualiza la pantalla
    screen.fill(white)
    screen.blit(ball, ballrect)
    pygame.display.flip()
#Salir del juego
pygame.quit()