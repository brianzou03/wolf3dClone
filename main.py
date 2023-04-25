import pygame as pg
import sys
from settings import *
from map import *

class Game:
    def __init__(self):  # Game constructor
        pg.init()  # initialize pygame
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)

    def update(self):  # update our screen and display current FPS
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps()}')  # current FPS

    def draw(self):  # at each iteration, paint the screen black
        self.screen.fill('black')
        self.map.draw()  # draw map

    def check_events(self):
        for event in pg.event.get():
            # escape key exits the game
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):  # while game is running, update the display and draw the screen
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
