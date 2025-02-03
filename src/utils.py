import random
from typing import List, Tuple
import src.enemies as enemies


def load_level(file_path: str) -> Tuple[List[List[str]], List[int], List[List[int]], List[enemies.Enemy]]:
    grid: List[List[str]] = []
    player_pos: List[int] = []
    portal_pos: List[List[int]] = []
    enemy_list: List[enemies.Enemy] = []

    with open(file_path, 'r') as file:
        for row_index, line in enumerate(file):
            row = []

            for col_index, char in enumerate(line.strip()):
                if char == 'P':
                    player_pos = [row_index, col_index]
                    row.append('1')
                elif char == 'T':
                    portal_pos.append([row_index, col_index])
                    row.append(char)
                elif char == '1':
                    my_list = ['1'] * 5 + ['8'] + ['9']
                    row.append(random.choice(my_list))
                elif char in 'BbGg':
                    movement: List[int] = [0, 1] if char.isupper() else [1, 0]
                    enemy_type: int = 0 if char.lower() == 'b' else 1
                    enemy_list.append(enemies.Enemy([row_index, col_index], movement, enemy_type))
                    row.append('1')
                else:
                    row.append(char)
            grid.append(row)

    return grid, player_pos, portal_pos, enemy_list
