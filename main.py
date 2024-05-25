import pygame

import settings


class Game:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()
        self.settings.new_game()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.settings.quit()

            if event.type == pygame.KEYDOWN:
                self.settings.toggle_controls(event)

    def update(self):

        for planet in self.settings.planets:
            planet.update()

        pygame.display.set_caption(f'{self.settings.clock.get_fps():.1f}')

    def draw(self):
        self.settings.screen.fill((30, 30, 30))
        for planet in self.settings.planets:
            planet.draw()

        self.settings.draw_selected_trail()

        pygame.display.update()

    def run(self):
        while True:
            self.events()
            if self.settings.running:
                self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
