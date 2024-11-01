From InternPe-Internship
1. Connect Four Game in Python
2.Digital_Clock
3.Snake_Game
4.Tic_Toc_toe



## From connect_4.py

This is a command-line implementation of the classic Connect Four game using Python and NumPy. The game allows two players to take turns dropping pieces into a 7-column, 6-row grid. 
The goal is to connect four of their pieces in a row—horizontally, vertically, or diagonally.

Key Features:

Players alternate turns to select a column to drop their piece.
The game checks for valid moves and winning conditions after each turn.
The game ends when one player connects four pieces, and the result is displayed.



## From Digital_Clock

Digital Clock Application in Python
This is a digital clock application built using Python's Tkinter library. The application displays the current time, date, and day of the week in a user-friendly graphical interface.

Key Features:

Real-Time Clock: Updates every second to show the current time in a 12-hour format with AM/PM.
Date Display: Shows the current date in the format DD-MM-YYYY.
Day of the Week: Displays the current day (e.g., Monday, Tuesday).
How It Works:

The update() function updates the time, date, and day labels every second.
The application uses strftime from the time module to format the time and date.
A Tkinter main loop keeps the window running until the user closes it.


## From Snake_py

Snake Game in Python
This is a classic Snake game implemented in Python using the Pygame library. The player controls a snake that moves around the screen, consuming food to grow longer while avoiding collisions with itself.

Key Features:

Snake Movement: The snake can be controlled using the arrow keys to change direction.
Food Consumption: The snake grows longer each time it consumes food, and the score increases.
Collision Detection: The game resets if the snake collides with itself.
Wrapping: The snake can wrap around the screen edges, reappearing on the opposite side.
How It Works:

The game initializes a grid where the snake moves and food appears randomly.
The snake's position and length are tracked, and it grows as it consumes food.
The game runs in a loop, updating the display and checking for user input.
Controls:

Arrow Keys: Move the snake (Up, Down, Left, Right).
Requirements:

Pygame library must be installed. You can install it via pip
pip install pygame


## From Tic_toe_toe2

Tic-Tac-Toe Game with AI in Python
This is a command-line implementation of the classic Tic-Tac-Toe game where a player can compete against an AI opponent. The AI uses the Minimax algorithm to make optimal moves, ensuring a challenging gameplay experience.

Key Features:

Two Players: Play as 'X' against an AI opponent as 'O'.
AI Decision Making: The AI utilizes the Minimax algorithm with alpha-beta pruning for strategic moves.
Win Detection: The game checks for winning conditions after each move.
Tie Detection: The game identifies ties when the board is full without a winner.
How It Works:

The game board is represented as a 3x3 grid.
Players take turns to enter their moves by specifying row and column indices (0-2).
The AI automatically determines its move based on the current state of the board.
Gameplay Instructions:

Start the game; the player (X) and AI (O) will take turns.
The player inputs their move in the format: row column (e.g., 0 1).
The game ends when one player wins or if there’s a tie.
Requirements:

This game runs in a Python environment and requires no external libraries.
