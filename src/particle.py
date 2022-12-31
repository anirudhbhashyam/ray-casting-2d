from dataclasses import dataclass, field

import numpy as np

import pygame

from ray import Ray


# Forward declaration for type hinting.
class Boundary:
    pass


@dataclass
class Particle:
    pos: np.ndarray[np.float32]
    radius: float
    rays: list[Ray] = field(
        default_factory = list
    )
    intersections: list[np.ndarray[np.float32]] = field(
        default_factory = list
    )
    color: tuple[int, int, int] = (255, 255, 255)

    def __post_init__(self) -> None:
        for i in range(0, 360, 10):
            angle_dir = np.array(
                [np.cos(np.radians(i)), np.sin(np.radians(i))],
                dtype = np.float32
            )
            self.rays.append(
                Ray(pos = self.pos, direction = angle_dir)
            )

    def look(self, walls: list[Boundary]) -> None:
        self.intersections.clear()
        for ray in self.rays:
            min_so_far = float("inf")
            record = None
            for wall in walls:
                intersection = ray.cast(wall)
                if intersection is not None:
                    d = np.linalg.norm(intersection - self.pos)
                    if d < min_so_far:
                        record = intersection
                        min_so_far = d
            if record is not None:
                self.intersections.append(record)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.ellipse(
            screen,
            self.color,
            (*[float(x) for x in self.pos], self.radius, self.radius)
        )

        for ray in self.rays:
            ray.draw(screen)

    def update(self, x: float, y: float) -> None:
        self.pos = np.array([x, y], dtype = np.float32)
        for ray in self.rays:
            ray.pos = self.pos