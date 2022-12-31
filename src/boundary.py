from dataclasses import dataclass, field

import pygame

import numpy as np


@dataclass
class Boundary:
    a: np.ndarray[np.float32]
    b: np.ndarray[np.float32]
    color: tuple[int, int, int] = (255, 255, 255)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.aaline(
            screen,
            (255, 255, 255),
            self.a,
            self.b
        )