import arcade
from Component import Component
class AnimationComponent(Component):
    x_start = 0
    x_steps = 0
    y_start = 0
    y_steps = 0

    offset = 0
    fps = 10
    current_frame = 0

    current_x = 1
    current_y = 1

    def __init__(self, x_start, y_start, x_steps, y_steps, offset):
        self.x_start = x_start
        self.x_steps = x_steps
        self.y_start = y_start
        self.y_steps = y_steps
        self.offset = offset


    def getCurrent(self):
        return (self.x_start + (self.current_x * self.offset), self.y_start + (self.current_y * self.offset))

    def update(self):
        self.current_frame += 1
        if(self.current_frame % self.fps is not 0):
            return
        else:
            print("Animation!")
            self.current_frame = 0;
        if(self.current_x == self.x_steps):
            self.current_x = 1
        else:
            self.current_x += 1

        if(self.current_y == self.y_steps):
            self.current_y = 1
        else:
            self.current_y += 1
