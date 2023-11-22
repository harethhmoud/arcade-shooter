import pygame
import initialization as init
import gun

points = 0
# shot = False
time_elapsed = 0
time_passed = 0


def draw_level(points):
    if init.level == 1 or init.level == 2:
        hit_boxes = [[], [], []]
    else:
        hit_boxes = [[], [], [], []]
    for i in range(len(points)):
        for j in range(len(points[i])):  # Creating a hit-box based off what tier of enemy we are on
            hit_boxes[i].append(pygame.rect.Rect((points[i][j][0] + 20, points[i][j][1]),
                                                 (60 - i * 12, 60 - i * 12)))
            init.screen.blit(init.target_images[init.level - 1][i], points[i][j])
    return hit_boxes


# initialize enemy coordinates

one_coordinates = [[], [], []]
two_coordinates = [[], [], []]
three_coordinates = [[], [], [], []]  # Coz level three has four enemies

# Getting a coordinate for every enemy we defined in our dictionary
for i in range(3):  # So we can store the three birds in coordinates
    a_list = init.targets[1]
    for j in range(a_list[i]):  # For the kind of bird, we create x and y coordinate based on what tier of enemy it is
        one_coordinates[i].append((init.WIDTH // (a_list[i]) * j, 300 - (i * 150) + 30 * (j % 2)))
for i in range(3):
    a_list = init.targets[2]
    for j in range(a_list[i]):
        two_coordinates[i].append((init.WIDTH // (a_list[i]) * j, 300 - (i * 150) + 30 * (j % 2)))
for i in range(4):
    a_list = init.targets[3]
    for j in range(a_list[i]):
        three_coordinates[i].append((init.WIDTH // (a_list[i]) * j, 300 - (i * 100) + 30 * (j % 2)))


def move_enemies(points):
    if init.level == 1 or init.level == 2:
        max_value = 3
    else:
        max_value = 4
    for i in range(max_value):
        for j in range(len(points[i])):
            a_coordinates = points[i][j]
            if a_coordinates[0] > -150:
                points[i][j] = (a_coordinates[0] - 2 ** i, a_coordinates[1])  # The higher the tier of the enemy, the
                # faster it is
            else:
                points[i][j] = (init.WIDTH, a_coordinates[1])  # If enemy goes off-screen to left, move it to right
    return points


def check_shot(targets, coordinates):
    global points
    mouse_position = pygame.mouse.get_pos()
    for x in range(len(targets)):
        for y in range(len(targets[x])):
            if targets[x][y].collidepoint(mouse_position):
                coordinates[x].pop(y)
                points += 10 + 10 * (i ** 2)  # The higher the enemy tier, the more points allocated
    return coordinates

def display_score():
    h = init.screen.get_height();
    points_text = init.font.render("Points: " + str(points), True, "black")
    init.screen.blit(points_text, (307, 665))
    shots_text = init.font.render("Total shots taken: " + str(gun.total_shots), True, "black")
    init.screen.blit(shots_text, (307, 692))
    time_text = init.font.render("Time elapsed: " + str(time_elapsed), True, "black")
    init.screen.blit(time_text, (307, 719))
    if gun.mode == 0:
        mode_text = init.font.render("Freeplay ", True, "black")
    elif gun.mode == 1:
        mode_text = init.font.render("Ammo remaining " + str(gun.ammo), True, "black")
    elif gun.mode == 2:
        mode_text = init.font.render("Time remaining " + str(time_passed), True, "black")
    init.screen.blit(mode_text, (307, 746))
