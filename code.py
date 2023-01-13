#!/usr/bin/env Python3
 
# Created By: Kestrel Bryce
# Date: Jan. 9, 2023
# This program is the "Space Aliens" program on the Pybadge
 
import ugame
import stage
import time
import random

# constants
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
TOTAL_NUMBER_OF_LASERS = 5
SHIP_SPEED = 1
ALIEN_SPEED = 1
LASER_SPEED = 2
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

game = stage.Stage(ugame.display, 60)
 
# import constants
def splash_scene():
    # This is the splash scene
    
    # Get coin sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    
    # Image bank
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # Setting background to image 0
    background = stage.Grid(image_bank_mt_background, SCREEN_X, SCREEN_Y)
    
    
    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white



    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white



    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white



    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white
    
   
    # game = stage.Grid(image_bank_mt_background, SCREEN_GRID_X, SCREEN_GRID_Y)
    game.layers = [background]
    game.render_block()
 
    while True:
        # Wait for 2 seconds
        time.sleep(2.0)
        menu_scene()
        
def menu_scene():
    # This is the main game scene
    
    
    # Button state
    button_state = {
        "button_up": "up",
        "button_just_pressed": "just pressed",
        "button_still_pressed": "still pressed",
        "button_released": "released"
    }
    
    # Palette for red coloured text
    RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
   
    # This function is the main game scene
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    
    
    # Add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Are You Sure?")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    # Sets the background to image 0 in Bank
    # Sets tile size
    background = stage.Grid(image_bank_background, SCREEN_GRID_X, SCREEN_GRID_Y)
   
    # Create stage for game
    # Set frame rate to 60 per second
    # game = stage.Stage(ugame.display, 60)
    game.layers = text + [background]
    game.render_block()
 
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_START != 0:
            game_scene()
       
        # Redraw Sprites
        game.tick()

def game_scene():
    
    # For score
    score = 0
    
    def show_alien():
        # This function takes an alien from off the screen and puts it on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + SPRITE_SIZE, SCREEN_X - SPRITE_SIZE), OFF_TOP_SCREEN)
                break
    
    # Button state
    button_state = {
        "button_up": "up",
        "button_just_pressed": "just pressed",
        "button_still_pressed": "still pressed",
        "button_released": "released"
    }
    
    # Palette for red coloured text
    # RED_PALETTE = (b'\xff\xff\x00\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    #                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff)
   
    # This function is the main game scene
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # State information buttons
    a_button = button_state["button_up"]
    b_button = button_state["button_up"]
    start_button = button_state["button_up"]
    select_button = button_state["button_up"]
    
    # Get sound ready
    pew_sound = open("pew.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
   
    # Sets the background to image 0 in Bank
    # Sets tile size
    background = stage.Grid(image_bank_background, SCREEN_GRID_X, SCREEN_GRID_Y)
    
    for x_location in range(SCREEN_GRID_X):
        for y_location in range(SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
   
    ship = stage.Sprite(image_bank_sprites, 5, 75, SCREEN_Y - (2 * SPRITE_SIZE))
    
    alien = stage.Sprite(image_bank_sprites, 9, int(SCREEN_X / 2 - SPRITE_SIZE / 2), 16)
    
    # Create list of aliens for they spawn
    aliens = []
    for alien_number in range(TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, OFF_SCREEN_X, OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    # Place one alien on the screen
    show_alien()
    
    # Create list of lasers for when we shoot
    lasers = []
    for laser_number in range(TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, OFF_SCREEN_X, OFF_SCREEN_Y)
        lasers.append(a_single_laser)
   
    # Create stage for game
    # Set frame rate to 60 per second
    game = stage.Stage(ugame.display, 60)
    game.layers = lasers + [ship] + aliens + [background]
    game.render_block()
 
    print("\n\n\n") # 3 blank lines
    print("Hello, World!")
 
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        
        # A button to fire
        if keys & ugame.K_X != 0:
            if a_button == button_state["button_up"]:
                a_button = button_state["button_just_pressed"]
            elif a_button == button_state["button_just_pressed"]:
                a_button = button_state["button_still_pressed"]
        else:
            if a_button == button_state["button_still_pressed"]:
                a_button = button_state["button_released"]
            else:
                a_button = button_state["button_up"]
        # B button
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= SCREEN_X - SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            # Sprite cannot go off screen
            else:
                ship.move(SCREEN_X - SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            # Sprite cannot go off screen
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
     
       
        # Update game logic
        if a_button == button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
                
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - LASER_SPEED)
                if lasers [laser_number].y < OFF_TOP_SCREEN:
                    lasers[laser_number].move(OFF_SCREEN_X, OFF_SCREEN_Y)
                    
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + ALIEN_SPEED)
                if aliens [alien_number].y < OFF_TOP_SCREEN:
                    aliens[alien_number].move(OFF_SCREEN_X, OFF_SCREEN_Y)
                    show_alien()
                    
        # Check if lasers are touching aliens
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x, lasers[laser_number].y,
                        lasers[laser_number].x + 16, lasers[laser_number].y + 16,
                        aliens[alien_number].x, aliens[alien_number].y,
                        aliens[alien_number].x + 16, aliens[alien_number].y + 16):
                            # Hitting an alien
                            aliens[alien_number].move(OFF_SCREEN_X, OFF_SCREEN_Y)
                            lasers[laser_number].move(OFF_SCREEN_X, OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
        
       
        # Redraw Sprites
        game.render_sprites(lasers + [ship] + aliens)
        game.tick()
 
if __name__ == "__main__":
    splash_scene()
