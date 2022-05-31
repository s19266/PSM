import pygame
import numpy as np
# import tkinter as tk

color_about_to_die = (200, 200, 225)
color_alive = (255, 255, 215)
color_background = (30, 30, 40)
color_grid = (30, 30, 60)

neighbor_keep_living_rule = {0:False, 1:False, 2:True, 3:True, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}
neighbor_birth_rule = {0:False, 1:False, 2:False, 3:True, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}

def update(surface, current, sz):
    nxt = np.zeros((current.shape[0], current.shape[1]))

    for r, c in np.ndindex(current.shape):
        num_alive = np.sum(current[r-1:r+2, c-1:c+2]) - current[r, c]
        if current[r, c] == 1 and neighbor_keep_living_rule[num_alive] == False:
            color = color_about_to_die
        elif (current[r, c] == 1 and neighbor_keep_living_rule[num_alive] == True) or (current[r, c] == 0 and neighbor_birth_rule[num_alive] == True):
            nxt[r, c] = 1
            color = color_alive

        color = color if current[r, c] == 1 else color_background
        pygame.draw.rect(surface, color, (c*sz, r*sz, sz-1, sz-1))
        

    return nxt

def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]);
    pos = (3,3)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells

def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    cells = init(dimx, dimy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(color_grid)
        cells = update(surface, cells, cellsize)

        pygame.display.update()
        # input("Press Enter to continue...")
if __name__ == "__main__":
    
    main(120, 90, 8)
