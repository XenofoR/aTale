import arcade
from Component import Component
class Change():
    change_x = 0
    change_y = 0

    def update_x(self,x):
        self.change_x = x

    def update_y(self,y):
        self.change_y = y

    def get_x(self):
        return self.change_x

    def get_y(self):
        return self.change_y

class MoveComponent(Component):
    movement = Change()
    new_x = 0
    new_y = 0

    def update(self):
        self.movement.update_x(self.new_x)
        self.movement.update_y(self.new_y)

    def getChangeClass(self):
        return self.movement
