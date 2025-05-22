import os
import json

WIDTH, HEIGHT = 725, 725
FPS = 100
SCALING_TANKS = 1.5
SCALING_BLOCKS = 1.75
SCALING_BULLET = 1.75

cell_size = WIDTH / 9.5

FIRE_INTERVAL = 1000
SPRITE_IMAGES = os.path.join(os.path.dirname(__file__), '..', 'sprite_images')
JSON_FILE = os.path.join(os.path.dirname(__file__), '..', 'tank_control.json')


def load_controls(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data["control"]