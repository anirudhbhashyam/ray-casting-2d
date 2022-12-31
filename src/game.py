from dataclasses import dataclass, field

import numpy as np

import pygame

from window import Window
from particle import Particle
from boundary import Boundary
from ray import Ray

@dataclass
class Game:
    fps: int
    window: Window
    clock: pygame.time.Clock = field(
        default_factory = pygame.time.Clock
    )

    def __post_init__(self) -> None:
        pygame.init()

    def run(self) -> None:
        running = True
        background_color = (30, 30, 30)

        p = Particle(
            pos = np.array([100, 100], dtype = np.float32),
            radius = 4.0
        )
        # ray = Ray(
        #     pos = np.array([100, 100], dtype = np.float32),
        #     direction = np.array([4, 3], dtype = np.float32)
        # )

        wall = Boundary(
            a = np.array([300, 200], dtype = np.float32),
            b = np.array([300, 600], dtype = np.float32)
        )

        while running:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running = False

            if not running:
                break

            self.window.fill_background(background_color)

            wall.draw(self.window.screen)
            p.draw(self.window.screen)


            for intersection in p.look([wall]):
                pygame.draw.aaline(
                    self.window.screen,
                    (255, 0, 0),
                    p.pos,
                    intersection
                )

            p.update(*pygame.mouse.get_pos())
            # for ray in p.rays:
            #     if ray.cast(wall):
            #         ray.color = (255, 0, 0)
            #     else:
            #         ray.color = (255, 255, 0)
            # t = ray.cast(wall)
            # if t is not None:
            #     ray.set_color((255, 0, 0))

            self.window.update()

        pygame.quit()

