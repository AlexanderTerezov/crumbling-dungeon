import pygame
from typing import List, Dict
from src.constants import TILE_SIZE, SCREEN_SCALE, WHITE, SCREEN_WIDTH
from src.enemies import Enemy


def draw_player(screen: pygame.Surface, player_pos: List[int], player_image: pygame.Surface) -> None:
    player_rect = pygame.Rect(player_pos[1] * TILE_SIZE, player_pos[0] * TILE_SIZE - 4 * SCREEN_SCALE, TILE_SIZE, TILE_SIZE)
    screen.blit(player_image, player_rect)

def draw_enemies(screen: pygame.Surface, enemy_list: List[Enemy], ghost_image: pygame.Surface, beholder_image: pygame.Surface) -> None:
    for enemy in enemy_list:
        enemy_rect = pygame.Rect(enemy.pos[1] * TILE_SIZE, enemy.pos[0] * TILE_SIZE - 4 * SCREEN_SCALE, TILE_SIZE, TILE_SIZE)
        screen.blit(ghost_image if enemy.pass_walls else beholder_image, enemy_rect)

def draw_screen(screen: pygame.Surface, grid: List[List[str]], player_pos: List[int], enemy_list: List[Enemy], images: Dict[str, pygame.Surface]) -> None:
    for row, line in enumerate(grid):
        for col, tile in enumerate(line):
            tile_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == '2':
                screen.blit(images["wall"], tile_rect)
            elif tile == '1':
                screen.blit(images["crumble_tile"], tile_rect)
            elif tile == '8':
                screen.blit(images["crumble_tile1"], tile_rect)
            elif tile == '9':
                screen.blit(images["crumble_tile2"], tile_rect)
            elif tile == '3':
                screen.blit(images["tile"], tile_rect)
            elif tile == 'E':
                screen.blit(images["exit"], tile_rect)
            elif tile == 'c':
                screen.blit(images["gold"], tile_rect)
            elif tile == 'C':
                screen.blit(images["chest"], tile_rect)
            elif tile == 'D':
                screen.blit(images["door"], tile_rect)
            elif tile == 'K':
                screen.blit(images["key"], tile_rect)
            elif tile == 'T':
                screen.blit(images["portal"], tile_rect)

    draw_player(screen, player_pos, images["player"])
    draw_enemies(screen, enemy_list, images["ghost"], images["beholder"])

def render_ui(screen: pygame.Surface, font: pygame.font.Font, score: int, score_to_add: int, current_level: int, lifes: int, heart_image: pygame.Surface):
    screen.blit(font.render( "SCORE: " + str(score + score_to_add) ,0,WHITE ),(10 * SCREEN_SCALE,10 * SCREEN_SCALE))
    screen.blit(font.render( "LEVEL: " + str(current_level+1) ,0,WHITE ),((SCREEN_WIDTH - 40 * SCREEN_SCALE),10 * SCREEN_SCALE))
    screen.blit(font.render( "x"+str(lifes) ,0,WHITE ),(22 * SCREEN_SCALE,25 * SCREEN_SCALE))
    heart_rect = pygame.Rect(6 * SCREEN_SCALE,20 * SCREEN_SCALE, TILE_SIZE, TILE_SIZE)
    screen.blit(heart_image, heart_rect)

