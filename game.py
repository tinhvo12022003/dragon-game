import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Dragon game")

clock = pygame.time.Clock()

background = pygame.image.load('img/bg.jpg')
background = pygame.transform.scale(background, (640, 480))

dragon = pygame.image.load('img/dragon.png')
dragon = pygame.transform.scale(dragon, (150, 150))
dragon_move_x = 320
dragon_move_y = 400

dragon_rect = dragon.get_rect(center=(dragon_move_x, dragon_move_y))

food = pygame.image.load('img/food.png')
food = pygame.transform.scale(food, (100, 100))
lst_pos_food = [i for i in range(80, 640, 80)]

gravity_food = 2.5

spawn_food = pygame.USEREVENT
pygame.time.set_timer(spawn_food, 1000)

lst_food = []

def create_food():
    food_rect = food.get_rect(midbottom=(random.choice(lst_pos_food), 0))
    return food_rect

def draw_food():
    for food_rect in lst_food:
        food_rect.y += gravity_food
        screen.blit(food, food_rect)

def collision_food():
    for food_rect in lst_food:
        if food_rect.colliderect(dragon_rect):
            lst_food.remove(food_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == spawn_food:
            lst_food.append(create_food())

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            dragon_rect.x -= 5

        if event.key == pygame.K_RIGHT:
            dragon_rect.x += 5

    screen.blit(background, (0, 0))
    screen.blit(dragon, dragon_rect)

    draw_food()
    collision_food()
    pygame.display.update()
    clock.tick(120)
