import pygame
import numpy as np

color_about_to_die = (200, 200, 225)
color_alive = (255, 255, 215)
color_background = (30, 30, 40)
color_grid = (30, 30, 60)

neighbor_keep_living_rule = {0:False, 1:False, 2:True, 3:True, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}
neighbor_birth_rule = {0:False, 1:False, 2:False, 3:True, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}

oscillators = [[2,2],[2,3],[2,4],[6,16],[6,17],[6,18],[7,16],[7,18],[8,16],[8,17],[8,18],[9,3],[9,4],[9,5],[9,16],[9,17],[9,18],[10,2],[10,3],[10,4],[10,16],[10,17],[10,18],[11,16],[11,17],[11,18],[12,16],[12,18],[13,16],[13,17],[13,18],[15,3],[15,4],[16,3],[16,4],[17,5],[17,6],[18,5],[18,6],[22,21],[22,22],[22,23],[22,27],[22,28],[22,29],[24,19],[24,24],[24,26],[24,31],[25,19],[25,24],[25,26],[25,31],[26,19],[26,24],[26,26],[26,31],[27,21],[27,22],[27,23],[27,27],[27,28],[27,29],[29,21],[29,22],[29,23],[29,27],[29,28],[29,29],[30,19],[30,24],[30,26],[30,31],[31,19],[31,24],[31,26],[31,31],[32,19],[32,24],[32,26],[32,31],[34,21],[34,22],[34,23],[34,27],[34,28],[34,29]]
spaceships = [[1,4],[1,10],[1,16],[1,22],[1,28],[1,34],[2,5],[2,11],[2,17],[2,23],[2,29],[2,35],[3,3],[3,4],[3,5],[3,9],[3,10],[3,11],[3,15],[3,16],[3,17],[3,21],[3,22],[3,23],[3,27],[3,28],[3,29],[3,33],[3,34],[3,35]],
gosper_glider_gun = [[3,27],[4,25],[4,27],[5,15],[5,16],[5,23],[5,24],[5,37],[5,38],[6,14],[6,18],[6,23],[6,24],[6,37],[6,38],[7,3],[7,4],[7,13],[7,19],[7,23],[7,24],[8,3],[8,4],[8,13],[8,17],[8,19],[8,20],[8,25],[8,27],[9,13],[9,19],[9,27],[10,14],[10,18],[11,15],[11,16]]
bi_gun = [[6,14],[7,13],[7,14],[8,12],[8,13],[9,13],[9,14],[9,17],[9,18],[10,41],[11,41],[11,42],[11,51],[11,52],[12,42],[12,43],[12,51],[12,52],[13,13],[13,14],[13,17],[13,18],[13,37],[13,38],[13,41],[13,42],[14,3],[14,4],[14,12],[14,13],[15,3],[15,4],[15,13],[15,14],[16,14],[17,37],[17,38],[17,41],[17,42],[18,42],[18,43],[19,41],[19,42],[20,41]]
# Only 2-3-8 / 3
oscillator_special = [[5,5],[5,8],[5,12],[5,13],[5,14],[6,6],[6,8],[6,12],[6,14],[7,6],[7,7],[7,8],[7,12],[7,15]]

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

def init(dim_x, dim_y):
    game_zone = np.zeros((dim_y, dim_x))

    init_pattern = np.zeros((35,60))
    
    # SELECTION OF DEFAULT CELLS
    for g in gosper_glider_gun:
        init_pattern[g[0],g[1]] = 1

    pos = (3,3)
    game_zone[pos[0]:pos[0] + init_pattern.shape[0], pos[1]:pos[1] + init_pattern.shape[1]] = init_pattern
    return game_zone

def main(dim_x, dim_y, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dim_x * cellsize, dim_y * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    game_zone = init(dim_x, dim_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(color_grid)
        game_zone = update(surface, game_zone, cellsize)

        pygame.display.update()
        # input("Press Enter to continue iteration...")
if __name__ == "__main__":
    main(120, 90, 8)
