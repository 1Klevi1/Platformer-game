import arcade
import arcade.gui

class Main_game(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
    ###
    # here will be the code for the first level
    ###
    def on_draw(self):
        self.clear()
        self.manager.draw()