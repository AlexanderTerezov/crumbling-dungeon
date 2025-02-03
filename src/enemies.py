from typing import List

class Enemy:
    def __init__(self, pos, movement, pass_walls):
        self.pos: List[int] = pos
        self.movement: List[int] = movement
        self.pass_walls: bool = pass_walls