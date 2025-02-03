import pygame
from src.constants import TILE_SIZE, SCREEN_SCALE
from typing import Dict


def load_images() -> Dict[str, pygame.Surface]:
    images: Dict[str, str] = {
        "tile": "images/tile.png",
        "crumble_tile1": "images/crumble_tile1.png",
        "crumble_tile2": "images/crumble_tile2.png",
        "crumble_tile": "images/crumble_tile.png",
        "wall": "images/wall.png",
        "player": "images/player.png",
        "exit": "images/exit_tile.png",
        "gold": "images/gold.png",
        "chest": "images/chest.png",
        "heart": "images/heart.png",
        "door": "images/door.png",
        "key": "images/key.png",
        "portal": "images/teleport.png",
        "ghost": "images/ghost.png",
        "beholder": "images/beholder.png",
    }

    scaled_images: Dict[str, pygame.Surface] = {
        name: pygame.transform.scale(pygame.image.load(path), (TILE_SIZE, TILE_SIZE))
        for name, path in images.items()
    }

    return scaled_images


def load_fonts() -> pygame.font.Font:
    pygame.font.init()
    return pygame.font.Font("fonts/monogram-extended.ttf", SCREEN_SCALE * 10)