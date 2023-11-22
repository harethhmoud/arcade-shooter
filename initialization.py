import pygame

pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 25)
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
backgrounds = []
banners = []
level = 0
guns = []
target_images = [[], [], []]
targets = {1: [10, 5, 3],
           2: [12, 8, 5],
           3: [15, 12, 8, 3]}
shot = False
counter = 0
menu = True
game_over = False
pause = False
menu_image = pygame.image.load("assets/menus/mainMenu.png")
game_over_image = pygame.image.load("assets/menus/gameOver.png")
pause_image = pygame.image.load("assets/menus/pause.png")

for i in range(1, 4):
    backgrounds.append(pygame.image.load("assets/backgrounds/" + str(i) + ".png"))
    banners.append(pygame.image.load("assets/banners/" + str(i) + ".png"))
    guns.append(pygame.transform.scale(pygame.image.load("assets/guns/" + str(i) + ".png"), (200, 200)))  # Gun size
    if i > 3:
        for j in range(1, 5):
            target_images[i - 1].append(pygame.transform.scale(
                pygame.image.load("assets/targets/" + str(i) + "/" + str(j)
                                  + ".png"), (120 - (j * 16), 80 - (j * 10))))
            # Making smaller enemies as we go through levels
    else:
        for j in range(1, 4):
            target_images[i - 1].append(pygame.transform.scale(
                pygame.image.load("assets/targets/" + str(i) + "/" + str(j)
                                  + ".png"), (120 - (j * 16), 80 - (j * 10))))
            # Making smaller enemies as we go through levels
