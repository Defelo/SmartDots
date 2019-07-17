from typing import List

from game import Game
from obstacle import Obstacle
from vector import Point


class Level:
    def __init__(self, start: Point, goal: Point, obstacles: List[Obstacle], checkpoints: List[Point]):
        self.start: Point = start
        self.goal: Point = goal
        self.obstacles: List[Obstacle] = obstacles
        self.checkpoints: List[Point] = checkpoints

    def make_game(self, width: float, height: float):
        return Game(width, height, self.start, self.goal, self.obstacles, self.checkpoints)
