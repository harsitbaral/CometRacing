import pygame
import sys
import math
import random
from car import *
from background import *

pygame.init()
SW, SH = 1920, 1080
screen = pygame.display.set_mode((SW, SH), pygame.RESIZABLE)
pygame.display.set_caption("Comet Racing")
clock = pygame.time.Clock()

car_surface = pygame.image.load('assets/spacecar.png')
car_w, car_h = 164, 332
car_surface = pygame.transform.scale(car_surface, (int(car_w / 2), int(car_h / 2)))

car = Car(SW / 2, SH / 2, car_surface)
car_group = pygame.sprite.GroupSingle(car)

star_group = pygame.sprite.Group()
STAR_EVENT = pygame.USEREVENT
pygame.time.set_timer(STAR_EVENT, 300)

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == STAR_EVENT:
            new_star = Star(random.randint(0, 1920), 0)
            star_group.add(new_star)

    screen.fill("#080738")

    car.speed *= 0.9  # 5
    if keys[pygame.K_UP]:
        car.speed += 0.5
    if keys[pygame.K_DOWN]:
        car.speed -= 0.5

    if keys[pygame.K_LEFT]:
        car.angle += car.speed / 2
    if keys[pygame.K_RIGHT]:
        car.angle -= car.speed / 2
    car.x -= car.speed * math.sin(math.radians(car.angle))
    car.y -= car.speed * math.cos(math.radians(-car.angle))

    car_group.update(screen)

    star_group.update()
    star_group.draw(screen)

    pygame.display.update()
    clock.tick(100)
