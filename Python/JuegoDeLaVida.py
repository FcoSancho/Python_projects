# Programando el juego de la vida

import sys, pygame
import numpy as np

pygame.init()

size = width, height = 600, 600

nX_cells = 60
nY_cells = 60

dimCW = (width - 1) / nX_cells
dimCH = (height - 1) / nY_cells

bg = 25, 25, 25

screen = pygame.display.set_mode(size)

screen.fill(bg)

gameState = np.random.randint(0, 2, (nX_cells, nY_cells))

print(gameState)

while 1:

  for y in range(0, nY_cells + 1):
    for x in range(0, nX_cells + 1):


      n_neigh = np.sum(gameState[x-1:x+2, y-1:y+2]) - gameState[x, y]

      print(n_neigh)


      np.sum(gameState[x-1:x+2, y-1:y+2]) - gameState[x, y]




      poly = [((x - 1) * dimCW, (y - 1) * dimCH),
              ((x) * dimCW,     (y - 1) * dimCH),
              ((x) * dimCW,     (y) * dimCH),
              ((x - 1) * dimCW, (y) * dimCH)]
      # pygame.draw.polygon(screen, (128, 128, 128), poly, 1)

  # pygame.display.flip()