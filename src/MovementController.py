import arcade
from MoveComponent import MoveComponent
class MovementController():
    movement_components = []

    def addComponent(self,c):
        self.movement_components.append(c)

    def update(self):
        for c in self.movement_components:
            c.update()
