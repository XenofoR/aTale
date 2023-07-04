import arcade
from Component import Component

class AnimationController:
    animation_components = []

    def addComponent(self, c):
        self.animation_components.append(c)

    def update(self):
        for c in self.animation_components:
            c.update()
