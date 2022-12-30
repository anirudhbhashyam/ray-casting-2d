from dataclasses import dataclass, field

import pygame

from window import Window

@dataclass
class Game:
    fps: int
    window: Window
    clock: pygame.time.Clock = field(
        default_factory = pygame.time.Clock
    )

    def __post_init__(self):
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

            self.window.fill_background(background_color)
            
            if not running:
                break

            self.window.update()
        return None

