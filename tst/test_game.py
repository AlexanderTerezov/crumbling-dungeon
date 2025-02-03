import unittest
import pygame
from src.constants import GRID_SIZE
from src.utils import load_level
from main import move_enemies, move_player
from src.enemies import Enemy
from typing import List

class TestGame(unittest.TestCase):

    def setUp(self):
        """Setup test environment before each test"""
        self.test_level = "levels/test_level.txt"
        self.grid, self.player_pos, self.portal_pos, self.enemy_list = load_level(self.test_level)
        self.keys = 0
        self.score_to_add = 0

    def test_load_level(self):
        """Test if the level loads correctly"""
        self.assertIsInstance(self.grid, list)
        self.assertIsInstance(self.player_pos, list)
        self.assertIsInstance(self.portal_pos, list)
        self.assertIsInstance(self.enemy_list, list)

    def test_enemy_movement(self):
        """Test enemy movement logic"""
        enemy_list: List[Enemy] = [Enemy([5, 5], [0, 1], False)] 
        move_enemies(enemy_list, self.grid)
        self.assertEqual(enemy_list[0].pos, [5, 6])

    def test_enemy_wall_collision(self):
        """Test enemy reverses direction on wall collision"""
        enemy_list: List[Enemy] = [Enemy([6, 7], [0, 1], False)]  # Next to a wall
        move_enemies(enemy_list, self.grid)
        self.assertEqual(enemy_list[0].movement, [0, -1])  # Should reverse

    def test_player_movement_valid(self):
        """Test player moves correctly on valid tiles"""
        event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT})
        old_pos = self.player_pos[:]
        player_pos, grid, score_to_add, keys = move_player(event, self.player_pos, self.grid, self.score_to_add, self.keys)
        self.assertNotEqual(old_pos, player_pos)  # Position should change

    def test_player_movement_wall_block(self):
        """Test player cannot move through walls"""
        event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT})
        old_pos = self.player_pos[:]
        player_pos, grid, score_to_add, keys = move_player(event, self.player_pos, self.grid, self.score_to_add, self.keys)
        self.assertEqual(old_pos, player_pos)  # Should remain the same


if __name__ == '__main__':
    unittest.main()
