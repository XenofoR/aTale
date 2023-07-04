import arcade
from MoveComponent import MoveComponent
class KeyController():
    player_controller = None
    def register_player(self, player_controller):
        self.player_controller = player_controller
    def parsePush(self, key):
        if key == arcade.key.UP:
            self.player_controller.new_y = 5
        elif key == arcade.key.DOWN:
            self.player_controller.new_y = -5
        elif key == arcade.key.LEFT:
            self.player_controller.new_x = -5
        elif key == arcade.key.RIGHT:
            self.player_controller.new_x = 5

    def parseRelease(self,key):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_controller.new_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_controller.new_x = 0
