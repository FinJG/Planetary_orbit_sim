import sys
from random import randint
from math import dist

import pygame

import objects


class Settings:
    def __init__(self) -> None:

        self.SCREEN_SIZE = pygame.Vector2(896, 896)

        self.FPS = 60  # float("inf") <- will remove the FPS cap
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        self.clock = pygame.time.Clock()
        self.dt = 1
        self.keys = pygame.key.get_pressed()

        self.planets = []
        self.currently_selected = 0

        self.COR = 0.90

        self.current_time = 0
        self.time_passed = 0
        self.slow = 1

        self.running = False

    @staticmethod
    def quit() -> None:
        """
        this function ends all processes and closes the game window
        """
        pygame.quit()
        sys.exit()

    def update_clock(self) -> None:
        """
        this function updates the clock and time related variables when called
        """
        self.current_time = self.time_passed
        self.time_passed += 1
        self.dt = self.clock.tick(self.FPS)

    def new_game(self) -> None:
        """
        this function clears and re-draws all planets on the map
        """
        self.planets.clear()

        # creates a planet in the center of the screen
        self.planets.append(objects.Planet(self,
                                           self.SCREEN_SIZE / 2,
                                           1_000_000_000,
                                           15,
                                           pygame.Vector2(0, 0),
                                           False)
                            )
        # randomly creates and places 10 planets
        self.randomly_place_planets(10)

    def randomly_place_planets(self, num: int) -> None:
        """
        this function will randomly place N planets onto the map
        :param num: the number of planets to place
        """
        x = int(self.SCREEN_SIZE.x)
        y = int(self.SCREEN_SIZE.y)
        for i in range(num):
            mass = randint(100, 1000)
            radius = int(mass * 0.01)
            pos = pygame.Vector2(randint(0, x), randint(0, y))
            velocity = pygame.Vector2(randint(-100, 100) / 500, randint(-100, 100) / 500)

            while True:
                if any([planet.radius + radius > dist(planet.pos, pos) for planet in self.planets]):
                    pos = pygame.Vector2(randint(0, x),
                                         randint(0, y))
                else:
                    self.planets.append(objects.Planet(self,
                                                       pos,
                                                       mass,
                                                       radius,
                                                       velocity)
                                        )
                    break

    def controls(self) -> None:
        """
        this function updates the controls that can be held down to use
        """
        self.keys = pygame.key.get_pressed()
        self.slow = 1
        if self.keys[pygame.K_x]:
            self.slow = 0.1

        if self.keys[pygame.K_z]:
            self.slow = 10

        if self.keys[pygame.K_w]:
            if self.current_time + 10 // self.slow < self.time_passed:
                self.current_time += int(10 // self.slow)
            else:
                self.current_time = self.time_passed

        if self.keys[pygame.K_s]:
            if self.current_time - 10 // self.slow > 0:
                self.current_time -= int(10 // self.slow)
            else:
                self.current_time = 0

    def toggle_controls(self, event=pygame.event.Event) -> None:
        """
        this function updates the controls that can be toggled to use
        :param event: the game events
        """
        if event.key == pygame.K_ESCAPE:
            self.quit()

        if event.key == pygame.K_r:
            self.new_game()

        if event.key == pygame.K_RIGHTBRACKET:
            if self.currently_selected - 0 >= 1:
                self.currently_selected -= 1

        if event.key == pygame.K_LEFTBRACKET:
            if self.currently_selected + 1 < len(self.planets):
                self.currently_selected += 1

        if event.key == pygame.K_RETURN:
            planet = self.planets[self.currently_selected]
            planet.drawing_path = not planet.drawing_path

        if event.key == pygame.K_SPACE:
            self.running = not self.running

    def draw_selected_trail(self):
        """
        draws the currently selected trail onto the screen
        """
        self.planets[self.currently_selected].draw_trail((255, 0, 0))
