import random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from config import *
from dot import Dot
from population import Population
from vector import Point

random.seed(0)


class SmartDots(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Dots")
        self.setFixedSize(WIDTH, HEIGHT)

        self.population: Population = Population(LEVEL.make_game(WIDTH, HEIGHT), POPULATION_SIZE)
        self.timer: QBasicTimer = QBasicTimer()
        self.timer.start(10, self)

        self.show()
        self.setFocus()

    def timerEvent(self, e: QTimerEvent):
        if e.timerId() == self.timer.timerId():
            self.tick()

    def tick(self):
        self.population.update()
        self.repaint()

    def keyReleaseEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Q:
            self.close()

    def paintEvent(self, _):
        qp: QPainter = QPainter(self)
        qp.setPen(Qt.white)
        qp.setBrush(Qt.white)
        qp.drawRect(self.rect())

        target: Point = self.population.game.get_current_target()

        qp.setPen(Qt.black)
        qp.setBrush(Qt.transparent)
        if self.population.best_dot is not None and not self.population.best_dot.reached_goal:
            radius: float = self.population.best_dot.closest_distance
            qp.drawEllipse(QPoint(*target), radius, radius)

        qp.setBrush([Qt.cyan, Qt.red][target == self.population.game.goal])
        qp.drawEllipse(QPoint(*self.population.game.goal), 5, 5)

        qp.setBrush(Qt.blue)
        for obstacle in self.population.game.obstacles:
            qp.drawRect(*obstacle.p1, *(obstacle.p2 - obstacle.p1))

        for checkpoint in self.population.game.checkpoints:
            qp.setBrush([Qt.cyan, Qt.red][target == checkpoint])
            qp.drawEllipse(QPoint(*checkpoint), 3, 3)

        for dot in self.population.dots[::-1]:  # type: Dot
            if dot.is_best:
                qp.setBrush(Qt.green)
                qp.drawEllipse(QPoint(*dot.pos), 4, 4)
            else:
                qp.setBrush(Qt.black)
                qp.drawEllipse(QPoint(*dot.pos), 2, 2)


if __name__ == '__main__':
    qa = QApplication([])
    app = SmartDots()
    qa.exec_()
