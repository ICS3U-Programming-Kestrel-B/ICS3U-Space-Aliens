#!/usr/bin/env Python3
 
# Created By: Kestrel Bryce
# Date: Jan. 9, 2023
# This program is the "Space Aliens" program on the Pybadge
 
import ugame
import stage
 
# import constants
def menu_scene():
    # This is the main game scene
    
    # constants
    SCREEN_X = 160
    SCREEN_Y = 128
    SCREEN_GRID_X = 10
    SCREEN_GRID_Y = 8
    SPRITE_SIZE = 16
    TOTAL_NUMBER_OF_ALIENS = 5
    FPS = 60
    SPRITE_MOVEMENT_SPEED = 1
    
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
    game = stage.Stage(ugame.display, 60)
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
    # constants
    SCREEN_X = 160
    SCREEN_Y = 128
    SCREEN_GRID_X = 10
    SCREEN_GRID_Y = 8
    SPRITE_SIZE = 16
    TOTAL_NUMBER_OF_ALIENS = 5
    FPS = 60
    SPRITE_MOVEMENT_SPEED = 1
    
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
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
   
    # Sets the background to image 0 in Bank
    # Sets tile size
    background = stage.Grid(image_bank_background, SCREEN_GRID_X, SCREEN_GRID_Y)
   
    ship = stage.Sprite(image_bank_sprites, 5, 75, SCREEN_Y - (2 * SPRITE_SIZE))
    
    alien = stage.Sprite(image_bank_sprites, 9, int(SCREEN_X / 2 - SPRITE_SIZE / 2), 16)
   
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
            sound.play(pew_sound)
       
        # Redraw Sprites
        game.render_sprites([ship] + [alien])
        game.tick()
 
if __name__ == "__main__":
    menu_scene()
