import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Dragon game")

clock = pygame.time.Clock()

background = pygame.image.load('img/bg.jpg').convert_alpha()
background = pygame.transform.scale(background, (640, 480))

dragon = pygame.image.load('img/dragon.png')
dragon = pygame.transform.scale(dragon, (150, 150))
dragon_move_x = 320
dragon_move_y = 400

dragon_rect = dragon.get_rect(center=(dragon_move_x, dragon_move_y))

food = pygame.image.load('img/food.png').convert_alpha()
food = pygame.transform.scale(food, (100, 100))
lst_pos_food = [i for i in range(80, 640, 80)]

gravity = 2.5

spawn_food = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_food, 500) 
lst_food = []

boom = pygame.image.load('img/boom.png').convert_alpha()
boom = pygame.transform.scale(boom, (100, 100))
lst_boom_pos = [i for i in range(80, 640, 80)]

spawn_boom = pygame.USEREVENT + 2
pygame.time.set_timer(spawn_boom, random.choice([i for i in range(1000, 10001, 2000)]))
lst_boom = []

def create_food():
    food_rect = food.get_rect(midbottom=(random.choice(lst_pos_food), 0))
    return food_rect

def draw_food():
    for food_rect in lst_food:
        food_rect.y += gravity
        screen.blit(food, food_rect)

def collision_food():
    for food_rect in lst_food:
        if food_rect.colliderect(dragon_rect) or food_rect.y >= 480:
            lst_food.remove(food_rect)
            

def create_boom():
    boom_rect = boom.get_rect(midbottom=(random.choice(lst_boom_pos), 0))
    return boom_rect

def draw_boom():

    for boom_rect in lst_boom:
        boom_rect.y += gravity
        screen.blit(boom, boom_rect)

def collision_boom():
    for boom_rect in lst_boom:
        if boom_rect.colliderect(dragon_rect):
            return False
    return True

score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or collision_boom() == False:
            print("Game over")
            pygame.quit()
            sys.exit()

        if event.type == spawn_food:
            lst_food.append(create_food())
        
        if event.type == spawn_boom:
            lst_boom.append(create_boom())

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            dragon_rect.x -= 5
        if event.key == pygame.K_RIGHT:
            dragon_rect.x += 5

    screen.blit(background, (0, 0))
    screen.blit(dragon, dragon_rect)

    collision_food()
    draw_food()
    draw_boom()
    pygame.display.update()
    clock.tick(120)
