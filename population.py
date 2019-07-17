import random
from typing import List

from config import CHECKPOINT_OPTIMIZATION_ROUNDS
from dot import Dot
from game import Game


class Population:
    def __init__(self, game: Game, size: int):
        self.game: Game = game
        self.dots: List[Dot] = [Dot.randomized(game) for _ in range(size)]
        self.total_fitness: float = 0
        self.best_dot: Dot = None

    def all_dots_dead(self) -> bool:
        return all(not dot.alive or dot.reached_goal for dot in self.dots)

    def calculate_fitness(self):
        self.total_fitness: float = 0
        for dot in self.dots:
            dot.calculate_fitness()
            self.total_fitness += dot.fitness

    def natural_selection(self):
        self.best_dot: Dot = max(self.dots, key=lambda dot: dot.fitness)
        new_dots: List[Dot] = [self.best_dot.clone()]
        new_dots[0].is_best = True

        for _ in range(1, len(self.dots)):
            new_dots.append(self.select_parent().clone())

        self.dots: List[Dot] = new_dots

    def select_parent(self):
        if self.game.target_countdown == 0:
            return self.best_dot

        rand: float = random.random() * self.total_fitness
        runner: float = 0
        for dot in self.dots:
            runner += dot.fitness
            if runner >= rand:
                return dot
        assert False, "math is broken"

    def mutate(self):
        if self.game.target_countdown == 0:
            self.game.mutation_start: int = self.best_dot.brain.step

        for dot in self.dots[1:]:
            dot.brain.mutate(self.game.mutation_start)

    def update(self):
        if self.all_dots_dead():
            self.calculate_fitness()
            self.natural_selection()
            self.mutate()
            print(f"Generation #{self.game.generation} complete!")
            if self.best_dot.reached_final_goal:
                self.game.mutation_start: int = 0
                print(f"  Reached goal in {self.best_dot.brain.step} steps!")
            elif self.best_dot.reached_goal:
                print(f"  Reached checkpoint #{self.game.current_target + 1} in {self.best_dot.brain.step} steps")
            print(f"  Best fitness: {self.best_dot.fitness}")
            print(f"  Average fitness: {self.total_fitness / len(self.dots)}")
            self.game.generation += 1

            if self.game.target_countdown is not None:
                if self.game.target_countdown > 0:
                    self.game.target_countdown -= 1
                else:
                    self.game.current_target += 1
                    self.game.target_countdown = None
            elif not self.best_dot.reached_final_goal and self.best_dot.reached_goal:
                self.game.target_countdown: int = CHECKPOINT_OPTIMIZATION_ROUNDS

            if self.game.target_countdown:
                print(f"  Optimizing this checkpoint for {self.game.target_countdown} more generations")
        else:
            for dot in self.dots:
                if self.best_dot and self.best_dot.reached_goal and dot.brain.step > self.best_dot.brain.step:
                    dot.die()
                else:
                    dot.update()
