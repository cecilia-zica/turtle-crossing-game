import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("White")
screen.tracer(0)

# --- Variables creation---
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

# --- Variables for continuous movement---
#Cars
moving_cars = False

#Player
moving_player = False

# - - - Functions for begin continuous movement - - -
def begin_mov_cars():
    global moving_cars
    moving_cars = True

def begin_mov_player():
    global moving_player
    moving_player = True

# - - - Funtions for stop continuous movement - - -
def stop_mov_player():
    global moving_player
    moving_player = False

def stop_mov_cars():
    global moving_cars
    moving_cars = False

# - - - Keyboard Input - - -
screen.listen()
screen.onkeypress(begin_mov_player, "Up")
screen.onkeyrelease(stop_mov_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if moving_player:
        player.move_up()

    # --- Collision detector ---
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # --- Sucessful crossing detector ---
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()