import random
import arcade
import pandas as pd

from apple import Apple
from snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=400, title="Super Snake 🐍 V2")
        arcade.set_background_color(arcade.color.KHAKI)
        self.snake=Snake(self)
        self.food=Apple(self)
        self.dataset=[]

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

        # data={"w0": None,
        #       "w1": None,
        #       "w2": None,
        #       "w3": None,
        #       "a0": None,
        #       "a1": None,
        #       "a2": None,
        #       "a3": None,
        #       "b0": None,
        #       "b1": None,
        #       "b2": None,
        #       "b3": None,
        #       "direction": None}

        data={"x_s": None,
              "y_s": None,
              "x_a": None,
              "y_a": None,
              "dx": None,
              "dy": None,
              "direction": None}

        dx= self.snake.center_x - self.food.center_x
        dy= self.snake.center_y - self.food.center_y

        data["x_s"]= self.snake.center_x
        data["y_s"]= self.snake.center_y
        data["x_a"]= self.food.center_x
        data["y_a"]= self.food.center_y
        data["dx"]= dx
        data["dy"]= dy
            
        if dx>0:
            if dy>0:
                self.snake.change_x=-1
                self.snake.change_y=-1
                data["direction"]= 5
            elif dy<0:
                self.snake.change_x=-1
                self.snake.change_y=1
                data["direction"]= 7
            else:
                self.snake.change_x=-1
                self.snake.change_y=0
                data["direction"]= 6

        if dx<0:
            if dy>0:
                self.snake.change_x=1
                self.snake.change_y=-1
                data["direction"]= 3
            elif dy<0:
                self.snake.change_x=1
                self.snake.change_y=1
                data["direction"]= 1
            else:
                self.snake.change_x=1
                self.snake.change_y=0
                data["direction"]= 2

        if dx==0:
            if dy>0:
                self.snake.change_x=0
                self.snake.change_y=-1
                data["direction"]= 4
            elif dy<0:
                self.snake.change_x=0
                self.snake.change_y=1
                data["direction"]= 0
            else:
                self.snake.change_x=0
                self.snake.change_y=0   

        self.dataset.append(data)


         

    
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food, 1)
            self.food=Apple(self)

        self.snake.check_pass_limits(self)


    def on_key_release(self, symbol: int, modifier: int):
        if symbol == arcade.key.Q:
            df = pd.DataFrame(self.dataset)
            df.to_csv("Output/dataset.csv", index= False)
            arcade.close_window()
            exit(0)

game=Game()
arcade.run()