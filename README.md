# Snake Game

This is a classic Snake Game built using Python's Turtle module. The player controls a snake that moves around the screen, eating food pellets to grow longer. The game ends if the snake collides with the boundaries of the screen or with itself.

## Features

- Classic snake gameplay.
- Two game modes: 'classic' and 'adan'.
- In 'classic' mode, the snake grows longer when it eats food.
- In 'adan' mode, obstacles appear on the screen, and the player must avoid them while collecting food.
- Persistent high score tracking.
- Modular code structure with separate modules for Snake, Food, ScoreBoard, and Obstacle.

## Setup

1. Make sure you have Python installed on your system.
2. Clone or download the repository to your local machine.
3. On the terminal type `pipenv install` and `pipenv shell` to setup the virtual enviroment
4. Run the main Python file to start the game: `python3 game/main.py`
5. Follow the on-screen instructions to choose a game mode and control the snake.

## Game Controls

- Use the arrow keys to control the snake's direction.
- Up arrow: Move the snake upwards.
- Down arrow: Move the snake downwards.
- Left arrow: Move the snake to the left.
- Right arrow: Move the snake to the right.

## Game Modes

### Classic Mode

- In this mode, the snake grows longer every time it eats food.
- The game ends if the snake collides with the screen boundaries or with itself.

### Adan Mode

- In this mode, obstacles appear on the screen, and the snake must avoid them while collecting food.
- Obstacles are generated randomly and increase in number as the player's score progresses.
- The game ends if the snake collides with an obstacle, the screen boundaries, or itself.

## Credits

- This game was created by [Adrian Cabrera].
- Inspired by classic Snake Games and adapted with additional features.
- Built using Python's Turtle module for graphics and user interaction.



