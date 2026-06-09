from turtle import Turtle,Screen
import random


screen = Screen()
screen.exitonclick()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter a Color: ").upper()
colors = ["red","orange","yellow3","green","blue","purple","turquoise"]
starting_position = [-100, -70, -40, -10, 20, 50, 80]
all_racer =[]


for i in range(0,7):
    t1 = Turtle(shape="turtle")
    t1.penup()
    t1.goto(x=-235,y=starting_position[i])
    t1.color(colors[i])
    all_racer.append(t1)

is_race_on = True

while is_race_on:
    for racer in all_racer:
        distance = random.randint(0,10)
        racer.forward(distance)
        if racer.xcor() > 225:
            screen.bye()
            winning_color = racer.pencolor().upper()
            if user_bet==winning_color:
                print(f"You have Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost!The {winning_color} turtle is the winner!")
            is_race_on = False
            break

