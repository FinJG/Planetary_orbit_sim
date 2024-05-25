from math import dist
from random import randint

from scipy.constants import gravitational_constant

import pygame


class Planet:
    def __init__(self, game, pos, mass, radius, initial_velocity=pygame.Vector2(), affected=True):
        self.game = game

        self.pos = pygame.Vector2(pos)
        self.velocity = initial_velocity
        self.mass = mass

        self.affected = affected

        self.col = (randint(100,255), randint(100,255), randint(100,255),)
        self.radius = radius

    def calc_new_velocity(self, planet):
        self.velocity = (((self.game.COR * planet.mass) * (planet.velocity - self.velocity)) + (
                (self.mass * self.velocity) + (planet.mass * planet.velocity))) / (self.mass + planet.mass)

        planet.velocity = (((self.game.COR * self.mass) * (self.velocity - planet.velocity)) + (
                (self.mass * self.velocity) + (planet.mass * planet.velocity))) / (self.mass + planet.mass)

    def collision(self):
        for planet in self.game.planets:
            if planet != self:
                if not dist(planet.pos, self.pos + self.velocity) > planet.radius + self.radius:
                    self.calc_new_velocity(planet)

    def update(self):
        self.velocity *= 0.99999

        if self.affected:
            for planet in self.game.planets:
                if planet != self:
                    g_force = (gravitational_constant * planet.mass * self.mass) / (dist(planet.pos, self.pos) ** 2)

                    self.velocity += (planet.pos - self.pos) * (g_force / self.mass)

        self.collision()
        self.pos += self.velocity

    def draw(self):
        pygame.draw.circle(self.game.display, self.col, self.pos, self.radius)
