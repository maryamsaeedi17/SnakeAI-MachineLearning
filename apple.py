import random
import arcade
from fruit import Fruit


class Apple(Fruit):
    def __init__(self,game):
        super().__init__()
        self.width=32
        self.height=32
        self.center_x=random.randint(16,game.width-16)
        self.center_y=random.randint(16,game.height-16)
        self.pic=arcade.load_texture("apple.png")

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x,self.center_y,self.width,self.height,self.pic)
        



