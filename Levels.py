import arcade
import arcade.gui
from arcade import Window

from Main_game import Main_game


class Levels(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.all_box=arcade.gui.UIBoxLayout()
        self.v_box=arcade.gui.UIBoxLayout()
        self.H_box=arcade.gui.UIBoxLayout(vertical=False,space_between= 10)

        level_text=arcade.gui.UIFlatButton(text=" LEVELS ", pressed=False)
        self.v_box.add(level_text.with_space_around(bottom=20))

        first_level=arcade.gui.UIFlatButton(text=" 1 ", width=200)
        self.H_box.add(first_level.with_space_around(bottom=20))
        first_level.on_click = self.on_click_first_level

        second_level=arcade.gui.UIFlatButton(text=" 2 ",width=200)
        self.H_box.add(second_level.with_space_around(bottom=20))
        second_level.on_click = self.on_click_second_level

        self.all_box.add(self.v_box)
        self.all_box.add(self.H_box)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="top",
                child=self.all_box)
            )
    def on_click_first_level(self, event):
        main_game_view = Main_game()
        arcade.Window.show_view(self.window,main_game_view)

    def on_click_second_level(self,event):
        main_game_view=Main_game()
        arcade.Window.show_view(self.window, main_game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()
