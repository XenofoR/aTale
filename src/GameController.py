import arcade
from RenderController import RenderController
from SpriteComponent import SpriteComponent
from KeyController import KeyController
from MoveComponent import MoveComponent
from MovementController import MovementController
# Set constants for the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ASSET_FOLDER = "../assets/"

class GameController(arcade.Window):

    renderer = RenderController()
    movement = MovementController()
    controller = KeyController()
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        player_change = MoveComponent()
        hero = SpriteComponent(ASSET_FOLDER+"Valkyrie.png",width=25,height=25, scale=2, x_position=450, y_position=300, offset_x=10, offset_y=3, movement=player_change)
        grass = SpriteComponent(ASSET_FOLDER+"grass.png",scale=4, width=425,height=425)
        self.renderer.addComponent(grass)
        self.renderer.addComponent(hero)
        self.movement.addComponent(player_change)
        self.controller.register_player(player_change)
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        self.renderer.draw()


    def on_update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.movement.update()
        self.renderer.update()



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        self.controller.parsePush(key)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        self.controller.parseRelease(key)


def main():
    game = GameController(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
