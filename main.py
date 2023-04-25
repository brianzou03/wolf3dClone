import pygame as pg
import sys
from settings import *
from map import *
from player import *

class Game:
    def __init__(self):  # Game constructor
        pg.init()  # initialize pygame
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1  # Delta Time: the amount of time that has passed since the last frame
        self.new_game()

    # on the start of a new game initialize map and player
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):  # update our screen and display current FPS
        self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps()}')  # current FPS

    def draw(self):  # at each iteration, paint the screen black
        self.screen.fill('black')
        self.map.draw()  # draw map
        self.player.draw()

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
