import math
import pygame
import initialization as init

total_shots = 0
ammo = 0
mode = 0


def draw_gun():
    mouse_position = pygame.mouse.get_pos()
    gun_point = (init.WIDTH / 2, init.HEIGHT - 200)
    lasers = ["red", "pink", "green"]
    clicks = pygame.mouse.get_pressed()
    if mouse_position[0] == gun_point[0]:  # If slope is 0 when mouse is on center of screen
        slope = -10000  # To avoid error when dividing by 0
    else:
        slope = (mouse_position[1] - gun_point[1]) / (mouse_position[0] - gun_point[0])
    angle = math.atan(slope)  # Inverse tangent of slope of line gives angle between x-axis and that line
    rotation = math.degrees(angle)  # PyGame needs degrees so we convert to degrees
    if mouse_position[0] > (init.WIDTH / 2):
        gun = init.guns[init.level - 1]
        if mouse_position[1] < 600:  # 600 are shooting area and 200 are menu
            init.screen.blit(pygame.transform.rotate(gun, 270 - rotation), (init.WIDTH / 2 - 30, init.HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(init.screen, lasers[init.level - 1], mouse_position, 5)
    else:
        gun = pygame.transform.flip(init.guns[init.level - 1], True, False)  # Flipping the gun so it will not look
        # awkward when looking at left side of screen
        if mouse_position[1] < 600:  # 600 are shooting area and 200 are menu
            init.screen.blit(pygame.transform.rotate(gun, 90 - rotation), (init.WIDTH / 2 - 90, init.HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(init.screen, lasers[init.level - 1], mouse_position, 5)
