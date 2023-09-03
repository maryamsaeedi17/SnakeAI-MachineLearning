import arcade

class Fruit(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.change_x=0
        self.change_y=0
        self.pic=None