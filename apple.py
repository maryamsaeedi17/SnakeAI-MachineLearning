import random
import arcade
from fruit import Fruit


class Apple(Fruit):
    def __init__(self,game):
        super().__init__()
        self.width=32
        self.height=32
        # self.size=16
        # self.color=arcade.color.RED
        self.center_x=random.randint(16,game.width-16)//8 *8
        self.center_y=random.randint(16,game.height-16)//8 *8
        self.pic=arcade.load_texture("Input/apple.png")

    def draw(self):
        #arcade.draw_circle_filled(self.center_x, self.center_y, self.size, self.color)
        arcade.draw_lrwh_rectangle_textured(self.center_x, self.center_y, self.width, self.height, self.pic)
        



