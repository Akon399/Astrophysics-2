# Notes & Lecture by Akhona Njeje.
# Date : 6 Sept 2023.
# Topic : Planetary Simulation & Exo Planets.

import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planetary Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Lets draw & create a solar system.

class Planet:
    AU = 149.6e6 * 100   # Astronomical Unit.
    G = 6.67428e-11   # Gravity.
    SCALE = 250 / AU   # 1AU = 100pixels.
    TIMESTEP = 3600*24   # 1DAY.

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun =False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):

        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color, (x,y), self.radius)

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892*10**30)
    sun.sun = True
    planets = [sun]

    while run:
        clock.tick(60)
        #WIN.fill(WHITE)   # Our backround tunrs white, but lets leave to black.
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()

main() 