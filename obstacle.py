from vector import Point


class Obstacle:
    def __init__(self, p1: Point, p2: Point):
        self.p1: Point = p1
        self.p2: Point = p2

    def check_collision(self, p: Point) -> bool:
        return self.p1.x - 2 <= p.x <= self.p2.x + 2 and self.p1.y - 2 <= p.y <= self.p2.y + 2
