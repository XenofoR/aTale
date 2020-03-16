import arcade

# Set constants for the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Render(arcade.Window):


    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        x = 300
        y = 300
        radius = 200
        arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

        arcade.finish_render()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = Render(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
