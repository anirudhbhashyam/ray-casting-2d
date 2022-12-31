from dataclasses import dataclass, field, InitVar

import numpy as np

import pygame

from window import Window
from particle import Particle
from boundary import Boundary


@dataclass
class World:
    n_particles: InitVar[int]
    n_walls: InitVar[int]
    world_dimensions: InitVar[tuple[int, int]]
    particles: list[Particle] = field(
        default_factory = list
    )
    walls: list[Boundary] = field(
        default_factory = list
    )

    def __post_init__(self, n_particles, n_walls, world_dimensions) -> None:
        world_w, world_h = world_dimensions
        for _ in range(n_particles):
            self.particles.append(
                Particle(
                    pos = np.random.default_rng().uniform(0, world_h, size = 2),
                    radius = 4.0
                )
            )
        for _ in range(n_walls):
            self.walls.append(
                Boundary(
                    a = np.random.default_rng().uniform(0, world_w, size = 2),
                    b = np.random.default_rng().uniform(0, world_h, size = 2)
                )
            )

        # Add boundaries to the world.
        self.walls.extend(
            [
                Boundary(a = (0, 0), b = (world_w, 0)),
                Boundary(a = (world_w, 0), b = (world_w, world_h)),
                Boundary(a = (world_w, world_h), b = (0, world_h)),
                Boundary(a = (0, world_h), b = (0, 0))
            ]
        )

    def draw(self, screen: pygame.Surface) -> None:
        for wall in self.walls:
            wall.draw(screen)

        for particle in self.particles:
            particle.draw(screen)

        for particle in self.particles:
            for intersection in particle.intersections:
                pygame.draw.aaline(
                    screen,
                    (200, 0, 0),
                    particle.pos,
                    intersection
                )

    def update(self) -> None:
        for particle in self.particles:
            particle.update(*pygame.mouse.get_pos())

        for particle in self.particles:
            particle.look(self.walls)


@dataclass
class Game:
    fps: int
    window: Window
    world: World
    clock: pygame.time.Clock = field(
        default_factory = pygame.time.Clock
    )

    def __post_init__(self) -> None:
        pygame.init()

    def run(self) -> None:
        running = True
        background_color = (30, 30, 30)

        while running:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running = False

            if not running:
                break

            self.window.fill_background(background_color)

            self.world.draw(self.window.screen)
            self.world.update()

            self.window.update()

        pygame.quit()

