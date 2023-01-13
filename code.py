#!/usr/bin/env Python3
 
# Created By: Kestrel Bryce
# Date: Jan. 9, 2023
# This program is the "Space Aliens" program on the Pybadge
 
import ugame
import stage
 
# import constants
def game_scene():
    # constants
    SCREEN_X = 160
    SCREEN_Y = 128
    SCREEN_GRID_X = 10
    SCREEN_GRID_Y = 8
    SPRITE_SIZE = 16
    TOTAL_NUMBER_OF_ALIENS = 5
    FPS = 60
    SPRITE_MOVEMENT_SPEED = 1
   
    # This function is the main game scene
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
   
    # Sets the background to image 0 in Bank
    # Sets tile size
    background = stage.Grid(image_bank_background, SCREEN_GRID_X, SCREEN_GRID_Y)
   
    ship = stage.Sprite(image_bank_sprites, 5, 75, SCREEN_Y - (2 * SPRITE_SIZE))
   
    # Create stage for game
    # Set frame rate to 60 per second
    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()
 
    print("\n\n\n") # 3 blank lines
    print("Hello, World!")
 
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
       
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= SCREEN_X - SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            # Sprite cannot go off screen
            else:
                ship.move(SCREEN_X - SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            # Sprite cannot go off screen
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
     
       
        # Update game logic
       
        # Redraw Sprites
        game.render_sprites([ship])
        game.tick()
 
 
if __name__ == "__main__":
    game_scene()