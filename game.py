from typing import List

from obstacle import Obstacle
from vector import Point


class Game:
    def __init__(self, width: float, height: float, start: Point, goal: Point,
                 obstacles: List[Obstacle], checkpoints: List[Point]):
        self.width: float = width
        self.height: float = height
        self.start: Point = start
        self.goal: Point = goal
        self.obstacles: List[Obstacle] = obstacles
        self.checkpoints: List[Point] = checkpoints
        self.generation: int = 1
        self.current_target: int = 0
        self.target_countdown: int = None
        self.mutation_start: int = 0

    def get_current_target(self) -> Point:
        if self.current_target < len(self.checkpoints):
            return self.checkpoints[self.current_target]
        return self.goal
