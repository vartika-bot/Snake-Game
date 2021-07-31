from turtle import Screen, Turtle
from snke import Snake
from food import Food
from score import Score
import time


screen = Screen()
food = Food()
score = Score()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Mania")
screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True


while game_on:
    screen.update()
    time.sleep(0.15)
    snake.move()


     #Detecting food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()

     #Detecting Wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

screen.exitonclick()