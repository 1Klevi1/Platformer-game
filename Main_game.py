import arcade
import arcade.gui

class QuitButton(arcade.gui.UITextureButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()
class MyWindow(arcade.View):
    def __init__(self):
        super().__init__()

        self.background = arcade.load_texture(
            f"C:/Users/E-store/OneDrive/Desktop/Sprites_game_dev/bg.jpg"
        )

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # texture1 = arcade.load_texture(
        #     f"C:/Users/E-store/OneDrive/Desktop/Sprites_game_dev/art1.png",
        #     width=200,
        #     height=50,
        # )
        # texture2 = arcade.load_texture(
        #     f"C:/Users/E-store/OneDrive/Desktop/Sprites_game_dev/art2.png",
        #     width=200,
        #     height=50,
        # )
        # texture3 = arcade.load_texture(
        #     f"C:/Users/E-store/OneDrive/Desktop/Sprites_game_dev/art3.1.png",
        #     width=200,
        #     height=50,
        # )

        start_button = arcade.gui.UITextureButton(
            text="Start Game",
            width=200,
            # texture=texture2,
            style={
                "font_color": (0, 0, 0),
                "font_size": 20,
                "bold": True,
                "font_name": "Kenney Mini Square",
            },
        )
        self.v_box.add(start_button.with_space_around(bottom=20))
        # Assigning our on_buttonclick() function
        # start_button.on_click = self.on_buttonclick

        settings_button = arcade.gui.UITextureButton(
            text="Settings",
            width=200,
            # texture=texture1,
            style={
                "font_color": (
                    0,
                    0,
                    0,
                ),
                "font_size": 18,
                "bold": True,
            },
        )
        self.v_box.add(settings_button.with_space_around(bottom=20))

        # Again, method 1. Use a child class to handle events.
        quit_button = QuitButton(
            text="Quit",
            width=200,
            # texture=texture3,
            style={"font_color": (0, 0, 0), "font_size": 18, "bold": True},
        )
        self.v_box.add(quit_button)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.v_box
            )
        )

    def on_draw(self):
        arcade.start_render()

        # Drawing the background image
        arcade.draw_texture_rectangle(300, 300, 600, 600, self.background)
        self.manager.draw()

    # def on_buttonclick(self, event):
    #     instructions_view = InstructionView()
    #     window.show_view(instructions_view)

window = arcade.Window(600, 600)
start_view = MyWindow()
window.show_view(start_view)

# window_2 = arcade.Window(1200, 600)


arcade.run()