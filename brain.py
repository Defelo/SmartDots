import random
from typing import List

from vector import Vector


class Brain:
    def __init__(self, size: int):
        self.step: int = 0
        self.size: int = size
        self.directions: List[Vector] = []

    def randomize(self):
        self.directions = [
            Vector(1, random.random() * 360) for _ in range(self.size)
        ]

    def available(self) -> bool:
        return self.step < self.size

    def next_direction(self) -> Vector:
        self.step += 1
        return self.directions[self.step - 1]

    def clone(self) -> 'Brain':
        out: Brain = Brain(self.size)
        out.directions = self.directions.copy()
        return out

    def mutate(self, start: int):
        mutation_rate: float = 0.01
        for i in range(start, self.size):
            if random.random() < mutation_rate:
                self.directions[i] = Vector(1, random.random() * 360)
