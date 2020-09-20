import arcade
from MoveComponent import MoveComponent
class KeyController():
    player_controller = None
    def register_player(self, player_controller):
        self.player_controller = player_controller
    def parsePush(self, key):
        if key == arcade.key.UP:
            print("key up")
            self.player_controller.new_y = 10
        elif key == arcade.key.DOWN:
            print("key down")
            self.player_controller.new_y = -10
        elif key == arcade.key.LEFT:
            print("key left")
            self.player_controller.new_x = -10
        elif key == arcade.key.RIGHT:
            print("key right")
            self.player_controller.new_x = 10

    def parseRelease(self,key):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_controller.new_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_controller.new_x = 0
