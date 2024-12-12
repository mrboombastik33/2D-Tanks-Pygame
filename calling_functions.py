import pygame as pg
from My_Project_OOP.additional.Direction import Direction
from My_Project_OOP.additional.settings import *

def load_controls(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data["control"]

def get_tank_direction(key, number):
    tank1, tank2 = load_controls(JSON_FILE)
    tank_controls = tank1 if number == 1 else tank2
    direction = 0

    if key[tank_controls["KEY_UP"]]:
        direction = Direction.UP
    elif key[tank_controls["KEY_DOWN"]]:
        direction = Direction.DOWN
    elif key[tank_controls["KEY_LEFT"]]:
        direction = Direction.LEFT
    elif key[tank_controls["KEY_RIGHT"]]:
        direction = Direction.RIGHT
    return direction


def tank_shoot(tank, key):
    current_time = pg.time.get_ticks()

    shooter1, shooter2 = load_controls(JSON_FILE)
    tank_controls = shooter1 if tank.number == 1 else shooter2

    if key[tank_controls["SHOOT"]] and current_time - tank.last_fire_time >= FIRE_INTERVAL:
        tank.last_fire_time = current_time
        bullet = tank.fire(f'{SPRITE_IMAGES}/bulletBlue1.png') if tank.number == 1 else tank.fire(f'{SPRITE_IMAGES}/bulletRed1.png')
        return bullet
    return None





