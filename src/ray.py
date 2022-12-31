from dataclasses import dataclass, field

import pygame

import numpy as np


# Forward declaration for type hinting.
class Boundary:
    ...


@dataclass
class Ray:
    pos: np.ndarray[np.float32]
    direction: np.ndarray[np.float32]
    color: tuple[int, int, int] = (255, 255, 0)

    def cast(self, wall: Boundary) -> np.ndarray[float] | None:
        x1, y1 = self.pos
        x2, y2 = self.pos + self.direction
        x3, y3 = wall.a
        x4, y4 = wall.b

        t_num = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        u_num = (x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return None

        t = t_num / den
        u = u_num / den

        if 0 <= u <= 1 and t >= 0:
            return np.array([x1 + t * (x2 - x1), y1 + t * (y2 - y1)], dtype = np.float32)

        return None

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.aaline(
            screen,
            self.color,
            self.pos,
            self.pos + self.direction * 50
        )

    def set_color(self, color: tuple[int, int, int]) -> None:
        self.color = color