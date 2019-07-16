from brain import Brain
from game import Game
from vector import Point, Vector


class Dot:
    def __init__(self, game: Game):
        super().__init__()

        self.fitness: float = 0
        self.is_best: bool = False
        self.alive: bool = True
        self.brain: Brain = Brain(1000)
        self.game: Game = game
        self.pos: Point = game.start
        self.vel: Vector = Vector(0, 0)
        self.closest_distance: float = 1e1337

        self.reached_goal: bool = False
        self.reached_final_goal: bool = False

    @staticmethod
    def randomized(game: Game) -> 'Dot':
        dot: Dot = Dot(game)
        dot.brain.randomize()
        return dot

    def die(self):
        self.alive: bool = False

    def move(self):
        if not self.brain.available():
            self.die()
            return

        acc: Vector = self.brain.next_direction()
        self.vel += acc
        self.vel.distance = min(self.vel.distance, 5)
        self.pos += self.vel.to_point()

    def update(self):
        if not self.alive or self.reached_goal:
            return

        self.move()
        current_target: Point = self.game.get_current_target()
        if self.brain.step >= self.game.mutation_start:
            self.closest_distance: float = min(self.closest_distance, (self.pos - current_target).to_vector().distance)

        if not (2 <= self.pos.x < self.game.width - 2 and 2 <= self.pos.y < self.game.height - 2):
            self.die()
        elif (self.pos - current_target).to_vector().distance < 5:
            if self.game.goal == current_target:
                self.reached_final_goal: bool = True
            self.reached_goal: bool = True
        elif any(obstacle.check_collision(self.pos) for obstacle in self.game.obstacles):
            self.die()

    def clone(self) -> 'Dot':
        out: Dot = Dot(self.game)
        out.brain = self.brain.clone()
        return out

    def calculate_fitness(self):
        if self.reached_goal:
            self.fitness: float = 10000 + 1 / (self.brain.step ** 2)
        else:
            self.fitness: float = 1 / (self.closest_distance ** 2)
