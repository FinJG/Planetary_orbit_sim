from math import dist
from random import randint

from scipy.constants import gravitational_constant

import pygame


class Planet:
    def __init__(self, settings, pos: pygame.Vector2, mass: int, radius: int, initial_velocity: pygame.Vector2, affected: bool = True) -> None:
        """
        this class creates a "planet" with a 'position', 'mass', 'radius' and 'initial_velocity'
        :param settings: the game settings
        :param pos: the planets initial position
        :param mass: the planets mass
        :param radius: the planets radius
        :param initial_velocity: the planets initial velocity
        :param affected: whether the planet is affected by gravity
        """
        self.settings = settings

        self.pos = pygame.Vector2(pos)
        self.velocity = initial_velocity
        self.mass = mass

        self.affected = affected

        self.col = (randint(100,255), randint(100,255), randint(100,255),)
        self.radius = radius

        self.trail = []
        self.display_trail = []
        self.steps = 0

        self.drawing_path = False

    def calc_new_velocity(self, planet) -> None:
        """
        this function calculates the new velocity of this planet, and the planet it has collided with
        :param planet: the planet that it has collided with
        """
        self.velocity = (((self.settings.COR * planet.mass) * (planet.velocity - self.velocity)) + (
                (self.mass * self.velocity) + (planet.mass * planet.velocity))) / (self.mass + planet.mass)

        planet.velocity = (((self.settings.COR * self.mass) * (self.velocity - planet.velocity)) + (
                (self.mass * self.velocity) + (planet.mass * planet.velocity))) / (self.mass + planet.mass)

    def collision(self) -> None:
        """
        this functions handles the collision between this planet and others
        """
        for planet in self.settings.planets:
            if planet != self:
                if not dist(planet.pos, self.pos + self.velocity) > planet.radius + self.radius:
                    self.calc_new_velocity(planet)

    def update(self) -> None:
        """
        this function is called to update the planet
        """
        self.velocity *= 0.99999

        if self.affected:
            for planet in self.settings.planets:
                if planet != self:
                    g_force = (gravitational_constant * planet.mass * self.mass) / (dist(planet.pos, self.pos) ** 2)

                    self.velocity += (planet.pos - self.pos) * (g_force / self.mass)

        self.collision()
        self.pos += self.velocity

        if self.steps % 1 == 0:
            self.trail.append(self.pos.copy())

        self.steps += 1

    def draw(self) -> None:
        """
        this function is called to draw the planet
        """
        pygame.draw.circle(self.settings.screen, self.col, self.pos, self.radius)
        if self.drawing_path:
            self.draw_trail(self.col)

    def draw_trail(self, colour) -> None:
        """
        this function is used to draw the planets 'trail'
        :param colour: the RBG colour of the trail
        """
        if len(self.trail[:self.settings.current_time]) > 2:
            pygame.draw.lines(self.settings.screen, colour, False, self.trail[:self.settings.current_time], 1)
            pygame.draw.circle(self.settings.screen, colour, self.trail[-1], self.radius)
