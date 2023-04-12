import pygame

pygame.init

WIN_WIDTH = 1280
WIN_HEIGHT = 768

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('EIA Frogger')


rec_width = 40
rec_height = 40
speed = 8
jump_height = 5
jumping = False
init_jump_height = jump_height
min_jump_height = -1 * jump_height
player_image = pygame.image.load("./assets/player/player.png")

x = int(WIN_WIDTH / 1 - rec_width / 3) # sets were the charecter will be spawned to
y = int(WIN_HEIGHT / 2 - rec_height / 3)

still_playing = True

while still_playing:
    pygame.time.delay(50) # frame setting

    for event in pygame.event.get(): # set up exit method
        if event.type == pygame.QUIT:
            still_playing = False

    keys = pygame.key.get_pressed() # controls, will be changed to work with joystick when base game is finished.

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed 
    elif keys[pygame.K_RIGHT] and x < WIN_WIDTH - rec_width:
        x += speed
    if not jumping:
        if keys[pygame.K_UP] and y > speed:
            y -= speed
        elif keys[pygame.K_DOWN] and y < WIN_HEIGHT - speed:
            y += speed
        elif keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_height >= min_jump_height: # jumping logic
            neg = 1
            if jump_height < 0:
                neg = -1
            y -= (jump_height ** 2) / 2 * neg
            jump_height -= 1
        else:
            jumping = False
            jump_height = init_jump_height

        if keys[pygame.K_ESCAPE]: # end process if ESC is pressed.
            pygame.quit()


    win.fill((0, 0, 0))
    #pygame.draw.rect(win, (255, 0, 0), (x, y, rec_width, rec_height)) // debug code
    win.blit(player_image, (x, y))
    pygame.display.update()
    

pygame.quit()