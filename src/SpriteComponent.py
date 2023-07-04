
from Component import Component
from MoveComponent import *
from AnimationComponent import *
import arcade
class SpriteComponent(Component):
    sprite = None
    movement = None
    animation = None
    def __init__(self, graphicResource, width, height, scale=1, x_position=0, y_position=0, offset_x=0, offset_y=0, movement=None, animation=None):
        self.sprite = arcade.Sprite(filename=graphicResource, scale=scale, center_x=x_position, center_y=y_position, image_width=width, image_height=height, image_x=offset_x, image_y=offset_y)
        self.movement = movement
        self.animation = animation
        self.update() #Run update to set initial sprite position

    def update(self):
        if(self.movement is not None):
            self.sprite.change_x = self.movement.getChangeClass().get_x()
            self.sprite.change_y = self.movement.getChangeClass().get_y()
        if(self.animation is not None):
            x,y = self.animation.getCurrent()
            print((self.sprite.image_x, self.sprite.image_y))
            print((x,y))
            self.sprite.image_x, self.sprite.image_y = self.animation.getCurrent()
        self.sprite.update()

    def set_x(self,x):
        self.sprite.center_x = x

    def set_y(self,y):
        self.sprite.center_y = y

    def draw(self):
        self.sprite.draw()
