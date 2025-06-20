# Turtle Crossing Game 🐢

Welcome to my version of the classic "Turtle Crossing" game! This project was developed as part of the **100 Days of Code** challenge, built entirely with Python and its native Turtle library.

The goal is simple: help our brave little turtle cross a busy road without getting squashed by the endless stream of cars.

### How to Play

* Use the **`Up Arrow`** key to move the turtle forward.
* Dodge the cars to safely reach the other side.
* With each successful crossing, the level increases, and the cars get faster!

### Tech Stack

* **Python 3**
* **Turtle Graphics Library**

### How to Run This Project

It's easy! You just need Python 3 installed on your system.

1.  First, clone this repository to your local machine:
    ```bash
    git clone [https://github.com/YOUR-USERNAME/turtle-crossing-game.git](https://github.com/YOUR-USERNAME/turtle-crossing-game.git)
    ```
2.  Navigate into the project directory:
    ```bash
    cd turtle-crossing-game
    ```
3.  Run the main file:
    ```bash
    python main.py
    ```
    And that's it! The game window should pop up, ready for you to play.

### Code Structure

The project is organized into modules to keep the code clean and understandable:

* `main.py`: The heart of the game. It controls the main game loop, the screen, and the interaction between all the objects.
* `player.py`: Defines the behavior of our turtle hero.
* `car_manager.py`: Responsible for creating, moving, and controlling the speed of the cars.
* `scoreboard.py`: Manages the score, the current level, and displaying the "Game Over" message.

---

Made with fun and lots of `import` statements during the 100 Days of Code challenge!