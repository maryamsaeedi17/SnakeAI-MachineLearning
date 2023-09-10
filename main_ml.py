import tensorflow as tf
import random
import arcade
import numpy as np

from apple import Apple
from snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=400, title="Super Snake 🐍 V2-ML")
        arcade.set_background_color(arcade.color.KHAKI)
        self.snake=Snake(self)
        self.food=Apple(self)
        self.model=tf.keras.models.load_model("weights/my_snake_model.h5")

        self.game_status="run"

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.food.draw()

        arcade.draw_text(f"Score: {self.snake.score}", 8*self.width//10, 20 , arcade.color.WHITE  , bold=True)

        if self.game_status=="Game Over":
            arcade.draw_lrtb_rectangle_filled(0, self.width, self.height, 0, arcade.color.BLACK)
            arcade.draw_text("GAME OVER!", self.width//5, self.height//2, arcade.color.RED, 30)

        arcade.finish_render()

    def on_update(self, delta_time: float):

        dx=self.snake.center_x - self.food.center_x
        dy=self.snake.center_y - self.food.center_y
       
        data = np.array([[self.snake.center_x, self.snake.center_y, self.food.center_x, self.food.center_y, dx, dy]])

        output=self.model.predict(data)
        direction= output.argmax()

        if direction==0:
            self.snake.change_x=0
            self.snake.change_y=1
        elif direction==1:
            self.snake.change_x=1
            self.snake.change_y=1
        elif direction==2:
            self.snake.change_x=1
            self.snake.change_y=0
        elif direction==3:
            self.snake.change_x=1
            self.snake.change_y=-1
        elif direction==4:
            self.snake.change_x=0
            self.snake.change_y=-1
        elif direction==5:
            self.snake.change_x=-1
            self.snake.change_y=-1
        elif direction==6:
            self.snake.change_x=-1
            self.snake.change_y=0
        elif direction==7:
            self.snake.change_x=-1
            self.snake.change_y=1

        self.snake.move()

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food, 1)
            self.food=Apple(self)

        self.snake.check_pass_limits(self)

game=Game()
arcade.run()