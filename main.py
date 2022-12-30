import os
import sys

CPD = os.path.abspath(
    os.path.join(
        os.path.abspath(__file__),
        *(1 * [os.pardir]),
    )
)

sys.path.append(
    os.path.join(CPD, "src")
)

import config
from window import Window
from game import Game

def main() -> int:
    config_settings = config.load(os.path.join(CPD, "config", "settings.json"))
    game_settings = config_settings["GAME_SETTINGS"]
    win = Window(
        width = game_settings["WIDTH"],
        height = game_settings["HEIGHT"],
        caption = game_settings["TITLE"]
    )
    g = Game(
        fps = game_settings["FPS"],
        window = win
    )
    g.run()
    return 0

if __name__ == "__main__":
    sys.exit(main())