import pygame
import math
import gun
import initialization as init
import level
import menu

run = True

while run:
    init.timer.tick(init.fps)
    if init.level != 0:
        if init.counter < 60:
            init.counter += 1
        else:
            init.counter = 1
            level.time_elapsed += 1
            if gun.mode == 2:
                level.time_passed -= 1
    init.screen.fill("black")
    init.screen.blit(init.backgrounds[init.level - 1], (0, 0))
    init.screen.blit(init.banners[init.level - 1], (0, init.HEIGHT - 200))
    if init.menu:
        init.level = 0
        menu.draw_menu()
    if init.game_over:
        init.level = 0
        menu.draw_game_over()
    if init.pause:
        init.level = 0
        menu.draw_pause()
    if init.level == 1:
        target_boxes = level.draw_level(level.one_coordinates)
        level.one_coordinates = level.move_enemies(level.one_coordinates)
        if init.shot is True:
            level.one_coordinates = level.check_shot(target_boxes, level.one_coordinates)
            init.shot = False
    elif init.level == 2:
        target_boxes = level.draw_level(level.two_coordinates)
        level.two_coordinates = level.move_enemies(level.two_coordinates)
        if init.shot is True:
            level.two_coordinates = level.check_shot(target_boxes, level.two_coordinates)
            init.shot = False
    elif init.level == 3:
        target_boxes = level.draw_level(level.three_coordinates)
        level.three_coordinates = level.move_enemies(level.three_coordinates)
        if init.shot:
            level.three_coordinates = level.check_shot(target_boxes, level.three_coordinates)
            init.shot = False
    if init.level > 0:
        gun.draw_gun()
        level.display_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            # Click inside game
            if (0 < mouse_position[0] < init.WIDTH) and (0 < mouse_position[1] < (init.HEIGHT - 200)):
                init.shot = True  # All good
                gun.total_shots += 1
                if gun.mode == 1:
                    gun.ammo -= 1
            if (670 < mouse_position[0] < 860) and (660 < mouse_position[1] < 715):
                menu.resume_level = level
                init.pause = True
            if (670 < mouse_position[0] < 860) and (715 < mouse_position[1] < 760):
                init.menu = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and menu.clicked:
            menu.clicked = False
    pygame.display.flip()
pygame.quit()
