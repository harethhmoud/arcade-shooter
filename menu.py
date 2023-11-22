import pygame.mouse

import initialization as init
import level
import gun

best_freeplay = 0
best_ammo = 0
best_timed = 0
clicked = False
write_values = False
#resume_level


def draw_menu():
    global best_ammo, best_timed, best_freeplay, write_values, clicked
    init.game_over = False
    init.pause = False
    init.screen.blit(init.menu_image, (0,0))
    mouse_position = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    freeplay_button = pygame.rect.Rect((170, 524), (260, 100))
    init.screen.blit(init.font.render(str(best_freeplay), True, "black"), (340, 587))
    ammo_button = pygame.rect.Rect((475, 524), (260, 100))
    init.screen.blit(init.font.render(str(best_ammo), True, "black"), (650, 587))
    timed_button = pygame.rect.Rect((170, 661), (260, 100))
    init.screen.blit(init.font.render(str(best_timed), True, "black"), (350, 715))
    reset_button = pygame.rect.Rect((475, 661), (260, 100))
    if freeplay_button.collidepoint(mouse_position) and clicks[0] and not clicked:
        gun.mode = 0
        init.level = 1
        init.menu = False
        level.time_elapsed = 0
        gun.total_shots = 0
        level.points = 0
        clicked = True
    if ammo_button.collidepoint(mouse_position) and clicks[0] and not clicked:
        gun.mode = 1
        init.level = 1
        init.menu = False
        level.time_elapsed = 0
        gun.ammo = 81
        gun.total_shots = 0
        level.points = 0
        clicked = True
    if timed_button.collidepoint(mouse_position) and clicks[0] and not clicked:
        gun.mode = 2
        init.level = 1
        init.menu = False
        level.time_elapsed = 0
        level.time_passed = 30
        gun.total_shots = 0
        level.points = 0
        clicked = True
    if reset_button.collidepoint(mouse_position) and clicks[0] and not clicked:
        best_freeplay = 0
        best_ammo = 0
        best_timed = 0
        write_values = True
        clicked = True


def draw_game_over():
    pass


def draw_pause():
    init.screen.blit(init.pause_image, (0, 0), )
    mouse_position = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    resume_button = pygame.rect.Rect((170, 661), (260, 100))
    menu_button = pygame.rect.Rect((475, 661), (260, 100))
    if resume_button.collidepoint(mouse_position) and clicks[0] and not clicked:
        init.level = resume_level

