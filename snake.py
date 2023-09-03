import arcade

class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width=32
        self.height=32
        self.center_x=game.width//2
        self.center_y=game.height//2
        self.color=arcade.color.ARMY_GREEN
        self.change_x=0
        self.change_y=0
        self.speed=3
        self.score=0
        self.body=[]

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

        # for part in self.body:
        #     if len(self.body)%2==0:
        #         arcade.draw_rectangle_filled(part['x'],part['y'],self.width,self.height,self.color)
        #     elif len(self.body)%2==1:
        #         arcade.draw_rectangle_filled(part['x'],part['y'],self.width,self.height,arcade.color.YELLOW)

        for i in range(len(self.body)):
            if i%2==0:
                arcade.draw_rectangle_filled(self.body[i]['x'],self.body[i]['y'],self.width,self.height,self.color)
            else:
                arcade.draw_rectangle_filled(self.body[i]['x'],self.body[i]['y'],self.width,self.height,arcade.color.YELLOW)


    def move(self):
        
        self.body.append({'x': self.center_x , 'y': self.center_y})
        
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        if len(self.body) > self.score:
            self.body.pop(0)

            
    def eat(self, food , score):
        del food
        self.score += score
        print("score:" , self.score)
        self.body.append({'x': self.center_x , 'y': self.center_y})


    def hit(self , food):
        del food
        if self.score>0:
            self.score -=1
        print("score:" , self.score)
        if len(self.body)>0:
            self.body.pop(-1)

    def check_pass_limits(self, game):
        if self.center_x<0 or self.center_x>game.width or self.center_y<0 or self.center_y>game.height:
            game.game_status="Game Over"
        