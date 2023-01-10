#!/usr/bin/env Python3

# Created By: Kestrel Bryce
# Date: Jan. 9, 2023
# This program is the "Space Aliens" program on the Pybadge

import ugame
import stage


def game_scene():
    # This function is the main game scene
    
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    print("\n\n\n") # 3 blank lines
    print("Hello, World!")

    while True:
        # Repeat forever, or until you turn it off!
        pass # just a place holder


if __name__ == "__main__":
    game_scene()