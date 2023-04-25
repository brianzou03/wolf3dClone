import pygame as pg

_ = False
# 1 = wall, _ = empty space
mini_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, 1, _, _, _, _, _, _, 1, 1],
            [1, _, _, 1, 1, 1, _, 1, _, _, 1, 1, 1, _, _, 1],
            [1, _, _, _, _, 1, _, 1, 1, _, 1, _, _, _, _, 1],
            [1, _, _, 1, 1, 1, _, _, _, _, 1, 1, 1, _, _, 1],
            [1, _, _, _, 1, _, _, _, _, _, _, _, 1, _, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Map class, an instance of Game class
class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    # Create the worldmap using numeric coordinates
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    # iterate over world map, drawing each element as an unfilled square
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]


