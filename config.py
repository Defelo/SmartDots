from level import Level
from obstacle import Obstacle
from vector import Point

WIDTH: int = 640
HEIGHT: int = 480

POPULATION_SIZE: int = 1000
CHECKPOINT_OPTIMIZATION_ROUNDS: int = 20

LEVEL: Level = [
    Level(
        Point(WIDTH / 2, HEIGHT - 10), Point(WIDTH / 2, 10), [
            Obstacle(
                Point(0, HEIGHT / 2 - 5),
                Point(WIDTH * 3 / 4, HEIGHT / 2 + 5)
            )
        ], []
    ), Level(
        Point(WIDTH / 2, HEIGHT - 10), Point(WIDTH / 2, 10), [
            Obstacle(
                Point(0, HEIGHT / 4 - 5),
                Point(WIDTH * 3 / 4 + 5, HEIGHT / 4 + 5)
            ), Obstacle(
                Point(WIDTH * 3 / 4 - 5, HEIGHT / 4 - 5),
                Point(WIDTH * 3 / 4 + 5, HEIGHT * 5 / 8 - 5)
            ), Obstacle(
                Point(WIDTH * 3 / 8, HEIGHT * 5 / 8 - 5),
                Point(WIDTH * 3 / 4 + 5, HEIGHT * 5 / 8 + 5)
            ), Obstacle(
                Point(WIDTH / 4, HEIGHT * 3 / 8 - 5),
                Point(WIDTH * 5 / 8, HEIGHT * 3 / 8 + 5)
            ), Obstacle(
                Point(WIDTH / 4 - 5, HEIGHT * 3 / 8 - 5),
                Point(WIDTH / 4 + 5, HEIGHT * 3 / 4 + 5)
            ), Obstacle(
                Point(WIDTH / 4 - 5, HEIGHT * 3 / 4 - 5),
                Point(WIDTH, HEIGHT * 3 / 4 + 5)
            )
        ], [
            Point(WIDTH / 2, HEIGHT * 2.5 / 8),
            Point(WIDTH / 2, HEIGHT * 4 / 8),
            Point(WIDTH / 2, HEIGHT * 5.5 / 8)
        ]
    )
][1]
