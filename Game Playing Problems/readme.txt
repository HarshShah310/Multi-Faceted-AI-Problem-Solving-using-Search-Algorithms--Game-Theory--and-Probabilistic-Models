Harsh Shah (1002057387)
----------------------------------
Programming Language: Python 3.12.2
------------------------------------------------
Code Structure:

1. Import Statement:
Imports the sys module for handling command-line arguments.

2. Class Definition: RedBlueNim:
Constructor __init__: Initializes the game parameters such as the number of red and blue marbles, game version, first player, and depth for the minimax algorithm.
Method switch_player: Switches the current player between human and computer.
Method play: Manages the game loop until it's over. In each iteration, it prints the current state, lets the current player make a move, and checks for the game's end condition.
Method computer_move: Implements the computer's move based on the minimax algorithm.
Method human_move: Takes input from the human player and validates their move.
Method update_board: Updates the game board based on the move made by the player.
Method minimax: Implements the minimax algorithm for the computer's move decision.
Method evaluate: Evaluates the current state of the game.
Method calculate_winner: Determines the winner of the game and prints the result.

3. Main Block:
Parses command-line arguments to initialize the game parameters.
Creates an instance of the RedBlueNim class with the provided parameters and starts the game by calling the play method.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to run the code:

1. Open the command prompt and use the cd command to change the current directory to the directory that contains the code file red_blue_nim.py and then use the following commands:
python red_blue_nim.py <num_red> <num_blue> <version> <first_player> <depth>
For example: python red_blue_nim.py 5 6 standard computer 5 (where red marbles are 5, blue marbles are 6, version is standard, first player will be computer, and depth is 5).

2. The game will start with the first player as computer, and you'll have to play the game until either the count of blue or red marbles reaches zero.

3. Once the game ends, the result will be generated, stating who won the game (human or computer) and their corresponding score.
