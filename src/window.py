from dataclasses import dataclass, field

import pygame


@dataclass
class Window:
    width: int
    height: int
    caption: str
    screen: pygame.Surface = field(
        init = False
    )
    main_font: pygame.font.Font = field(
        init = False
    )
    title_font: pygame.font.Font = field(
        init = False
    )

    def __post_init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.main_font = pygame.font.SysFont(
            "Arial", 20
        )
        self.title_font = pygame.font.SysFont(
            "Arial", 40
        )

    def fill_background(self, color: tuple[int, int, int]) -> None:
        self.screen.fill(color)

    @staticmethod
    def update() -> None:
        pygame.display.update()
