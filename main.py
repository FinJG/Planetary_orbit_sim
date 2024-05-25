import sys
from math import dist
from random import randint

import pygame as pygame

import objects


class Game:
    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 896
        self.SCREEN_HEIGHT = 896

        self.DISPLAY_WIDTH = self.SCREEN_WIDTH
        self.DISPLAY_HEIGHT = self.SCREEN_HEIGHT
        self.FPS = float("inf")

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

        self.clock = pygame.time.Clock()
        self.dt = 1

        self.planets = []
        self.new_game()
        self.COR = 0.94

    def new_game(self):
        self.planets.append(objects.Planet(self,
                                           (self.DISPLAY_WIDTH / 2, self.DISPLAY_HEIGHT / 2),
                                           1_000_000_000,
                                           75,
                                           pygame.Vector2(0, 0))
                            )

        for i in range(3):
            mass = randint(2, 100)
            pos = pygame.Vector2(randint(0, self.DISPLAY_WIDTH),randint(0, self.DISPLAY_HEIGHT))
            velocity = pygame.Vector2(randint(-20, 20) / 100, randint(-20, 20) / 100)
            while True:
                if any([planet.radius + mass > dist(planet.pos, pos) for planet in self.planets]):
                    pos = pygame.Vector2(randint(0, self.DISPLAY_WIDTH), randint(0, self.DISPLAY_HEIGHT))
                else:
                    break

            self.planets.append(objects.Planet(self,
                                               pos,
                                               mass,
                                               10,
                                               velocity)
                                )

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update(self):

        for planet in self.planets:
            planet.update()

        self.dt = self.clock.tick(self.FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.display.fill((30, 30, 30))
        for planet in self.planets:
            planet.draw()

        scaled_display = pygame.transform.scale(self.display, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.blit(scaled_display, (0, 0))
        pygame.display.update()

    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
