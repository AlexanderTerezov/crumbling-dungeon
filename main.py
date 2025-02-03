import pygame
from src.constants import *
from src.assets import load_images, load_fonts
from src.utils import load_level
from src.rendering import draw_screen, render_ui
from src.enemies import Enemy
from typing import List, Dict, Tuple

def move_enemies(enemy_list: List[Enemy], grid: List[List[str]]):
    for enemy in enemy_list:
        new_enemy_pos = [enemy.pos[0] + enemy.movement[0], enemy.pos[1] + enemy.movement[1]]

        if (0 <= new_enemy_pos[0] < GRID_SIZE and 0 <= new_enemy_pos[1] < GRID_SIZE):
            if grid[new_enemy_pos[0]][new_enemy_pos[1]] == '2':
                if not enemy.pass_walls:
                    enemy.movement = [-x for x in enemy.movement]
                    new_enemy_pos = [enemy.pos[0] + enemy.movement[0], enemy.pos[1] + enemy.movement[1]]
        else:
            enemy.movement = [-x for x in enemy.movement]
            new_enemy_pos = [enemy.pos[0] + enemy.movement[0], enemy.pos[1] + enemy.movement[1]]

        enemy.pos = new_enemy_pos

def move_player(event: pygame.event, player_pos: List[int], grid: List[List[str]], score_to_add: int, keys: int) -> Tuple[List[int], List[List[str]], int, int]:
    new_pos = player_pos[:]
    if event.key == pygame.K_LEFT:
        new_pos[1] -= 1
    elif event.key == pygame.K_RIGHT:
        new_pos[1] += 1
    elif event.key == pygame.K_UP:
        new_pos[0] -= 1
    elif event.key == pygame.K_DOWN:
        new_pos[0] += 1

    if (0 <= new_pos[0] < GRID_SIZE and 0 <= new_pos[1] < GRID_SIZE and grid[new_pos[0]][new_pos[1]] != '2' and new_pos != player_pos):
        # Door logic
        if grid[new_pos[0]][new_pos[1]] == 'D':
            if keys > 0:
                keys -= 1
                grid[new_pos[0]][new_pos[1]] = '1'
            else:
                return player_pos, grid, score_to_add, keys
        else:
            if grid[player_pos[0]][player_pos[1]] == '3':
                grid[player_pos[0]][player_pos[1]] = '1'
            elif grid[player_pos[0]][player_pos[1]] != 'T':
                grid[player_pos[0]][player_pos[1]] = '0'
            player_pos = new_pos
            score_to_add += 1

    return player_pos, grid, score_to_add, keys

def handle_collisions(player_pos: List[int], enemy_list: List[Enemy], grid: List[List[str]], lifes: int, score_to_add: int, portal_pos: List[List[int]]) -> Tuple[int, int, bool]:
    for enemy in enemy_list:
        if enemy.pos == player_pos:
            lifes -= 1
            score_to_add = 0
            return lifes, score_to_add, True

    if grid[player_pos[0]][player_pos[1]] == '0':  # Fell off the grid
        lifes -= 1
        score_to_add = 0
        return lifes, score_to_add, True

    return lifes, score_to_add, False

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Crumbling Dungeon")
    clock = pygame.time.Clock()

    images = load_images()
    font = load_fonts()

    current_level = 0
    lifes = 3
    score = 0
    score_to_add = 0
    keys = 0

    grid, player_pos, portal_pos, enemy_list = load_level(LEVELS[current_level])

    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN and event.key in KEYS:
                # Exit
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                # Move 
                old_player_pos = player_pos
                player_pos, grid, score_to_add, keys = move_player(event, player_pos, grid, score_to_add, keys)

                # Enemy Movement
                if player_pos != old_player_pos:
                    move_enemies(enemy_list, grid)
                
                # Check collisions
                lifes, score_to_add, reset = handle_collisions(player_pos, enemy_list, grid, lifes, score_to_add, portal_pos)

                # Check game over
                if reset:
                    if lifes <= 0:
                        current_level = 0
                        lifes = 3
                        score = 0
                        print("Game Over")
                    grid, player_pos, portal_pos, enemy_list = load_level(LEVELS[current_level])
                    continue

                # Handle special tiles

                if(grid[player_pos[0]][player_pos[1]] == 'E'):
                    print(f"You completed level {current_level + 1}!")
                    current_level += 1
                    score += score_to_add
                    score_to_add = 0
                    if current_level < len(LEVELS):
                        grid, player_pos, portal_pos, enemy_list = load_level(LEVELS[current_level])
                    else:
                        print("You completed all levels! Congratulations!")
                        print(f"Your score is {score}")
                        running = False
                
                if(grid[player_pos[0]][player_pos[1]] == 'c'):
                    score_to_add += 50
                    grid[player_pos[0]][player_pos[1]] = '1'

                if(grid[player_pos[0]][player_pos[1]] == 'C'):
                    score_to_add += 100
                    grid[player_pos[0]][player_pos[1]] = '1'

                if(grid[player_pos[0]][player_pos[1]] == 'K'):
                    keys += 1
                    grid[player_pos[0]][player_pos[1]] = '1'

                if(grid[player_pos[0]][player_pos[1]] == 'T'):
                    if player_pos == portal_pos[0]:
                        player_pos = portal_pos[1]
                    elif player_pos == portal_pos[1]:
                        player_pos = portal_pos[0]
            
            

        screen.fill(MAGENTA)
        draw_screen(screen, grid, player_pos, enemy_list, images)
        render_ui(screen, font, score, score_to_add, current_level, lifes, images['heart'])

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()