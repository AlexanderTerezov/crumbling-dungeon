import pygame

GRID_SIZE: int = 19
SCREEN_SCALE: int = 4
TILE_SIZE: int = 16 * SCREEN_SCALE
SCREEN_WIDTH: int = GRID_SIZE * TILE_SIZE
SCREEN_HEIGHT: int = GRID_SIZE * TILE_SIZE
LEVELS: list[str] = ["levels/level_1.txt", "levels/level_2.txt", "levels/level_3.txt", "levels/level_4.txt", "levels/level_5.txt", "levels/level_6.txt","levels/level_7.txt", "levels/level_8.txt", "levels/level_9.txt","levels/level_10.txt", "levels/level_11.txt"]
#LEVELS: list[str] = ["levels/level_10.txt"]

FPS: int = 60
KEYS: list[int] = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_ESCAPE]

MAGENTA: tuple[int, int, int] = (30, 21, 29)
WHITE: tuple[int, int, int] = (255, 255, 255)