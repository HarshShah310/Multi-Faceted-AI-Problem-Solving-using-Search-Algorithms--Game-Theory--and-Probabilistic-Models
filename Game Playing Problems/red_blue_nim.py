import sys

class RedBlueNim:
    def __init__(self, num_red, num_blue, version="standard", first_player="computer", depth=3):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.first_player = first_player
        self.depth = depth
        self.current_player = first_player
        self.game_over = False

    def switch_player(self):
        self.current_player = "computer" if self.current_player == "human" else "human"

    def play(self):
        while not self.game_over:
            print(f"\nCurrent State: {self.num_red} red marbles, {self.num_blue} blue marbles")
            if self.current_player == "computer":
                self.computer_move()
            else:
                self.human_move()
            if self.num_red == 0 or self.num_blue == 0:
                self.game_over = True
                print("\nGame Over!")
                self.calculate_winner()

    def computer_move(self):
        if self.version == "standard":
            moves = [(2, 'red'), (2, 'blue'), (1, 'red'), (1, 'blue')]
        else:
            moves = [(1, 'blue'), (1, 'red'), (2, 'blue'), (2, 'red')]

        best_score = float('-inf')
        best_move = None

        for move in moves:
            if move[1] == 'red' and self.num_red >= move[0]:
                new_red = self.num_red - move[0]
                new_blue = self.num_blue
            elif move[1] == 'blue' and self.num_blue >= move[0]:
                new_red = self.num_red
                new_blue = self.num_blue - move[0]
            else:
                continue

            score = self.minimax(new_red, new_blue, self.depth, False, float('-inf'), float('inf'))
            if score > best_score:
                best_score = score
                best_move = move

        print(f"Computer picks {best_move[0]} {best_move[1]} marble(s).")
        self.update_board(best_move)
        self.switch_player()

    def human_move(self):
        valid_move = False
        while not valid_move:
            move = input("Your move (e.g., '2 red'): ").split()
            if len(move) != 2:
                print("Invalid move. Please enter a valid move.")
                continue
            num, color = move
            if not num.isdigit():
                print("Invalid move. Please enter a valid move.")
                continue
            num = int(num)
            if color != "red" and color != "blue":
                print("Invalid move. Please enter a valid move.")
                continue
            if num not in [1, 2]:  # Ensure only 1 or 2 marbles can be picked
                print("Invalid move. Please enter a valid move.")
                continue
            if (color == "red" and num > self.num_red) or (color == "blue" and num > self.num_blue):
                print("Invalid move. Not enough marbles.")
                continue
            valid_move = True
            print(f"You picked {num} {color} marble(s).")
            self.update_board((num, color))
            self.switch_player()

    def update_board(self, move):
        num, color = move
        if color == 'red':
            self.num_red -= num
        else:
            self.num_blue -= num

    def minimax(self, num_red, num_blue, depth, is_maximizing_player, alpha, beta):
        if depth == 0 or num_red == 0 or num_blue == 0:
            return self.evaluate(num_red, num_blue)

        if is_maximizing_player:
            max_eval = float('-inf')
            moves = [(2, 'red'), (2, 'blue'), (1, 'red'), (1, 'blue')]
            for move in moves:
                if move[1] == 'red' and num_red >= move[0]:
                    new_red = num_red - move[0]
                    new_blue = num_blue
                elif move[1] == 'blue' and num_blue >= move[0]:
                    new_red = num_red
                    new_blue = num_blue - move[0]
                else:
                    continue
                eval = self.minimax(new_red, new_blue, depth - 1, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            moves = [(2, 'red'), (2, 'blue'), (1, 'red'), (1, 'blue')]
            for move in moves:
                if move[1] == 'red' and num_red >= move[0]:
                    new_red = num_red - move[0]
                    new_blue = num_blue
                elif move[1] == 'blue' and num_blue >= move[0]:
                    new_red = num_red
                    new_blue = num_blue - move[0]
                else:
                    continue
                eval = self.minimax(new_red, new_blue, depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def evaluate(self, num_red, num_blue):
        """
        Evaluate the current state of the game.

        Args:
            num_red (int): Number of remaining red marbles.
            num_blue (int): Number of remaining blue marbles.

        Returns:
            int: Evaluation score indicating the favorability of the current position for the computer player.
        """
        # We want to prioritize states where the opponent has fewer options to play,
        # especially if it's close to winning, so we penalize those states more heavily.

        # Weight for red marbles
        red_weight = 2

        # Weight for blue marbles
        blue_weight = 3

        # In standard Nim, having fewer marbles left is better.
        if self.version == "standard":
            return red_weight * num_red + blue_weight * num_blue

        # In Misère Nim, having more marbles left is better.
        else:
            return red_weight * (self.num_red - num_red) + blue_weight * (self.num_blue - num_blue)

    def calculate_winner(self):
        if self.version == "standard":
            # In the standard version, if any player has an empty pile, they lose
            if self.num_red == 0 or self.num_blue == 0:
                winner = "Human" if self.current_player == "computer" else "Computer"
            else:
                winner = "Computer" if self.current_player == "human" else "Human"
        else:  # Misère version
            # In the misère version, if any player has an empty pile, they win
            if self.num_red == 0 or self.num_blue == 0:
                winner = self.current_player.capitalize()
            else:
                winner = "Human" if self.current_player == "computer" else "Computer"

        if self.version == "standard":
            score = -2 * self.num_red - 3 * self.num_blue
        else:
            score = 2 * self.num_red + 3 * self.num_blue

        print(f"{winner} wins with a score of {abs(score)}.")

if __name__ == "__main__":
    args = sys.argv[1:]
    num_red = int(args[0])
    num_blue = int(args[1])
    version = args[2] if len(args) > 2 else "standard"
    first_player = args[3] if len(args) > 3 else "computer"
    depth = int(args[4]) if len(args) > 4 else 1

    game = RedBlueNim(num_red, num_blue, version, first_player, depth)
    game.play()