import random


class Minesweeper:
    def __init__(self):
        self.rows = 4
        self.cols = 4
        self.mines = 2
        self.game_board = []
        self.visible_board = []
        self.flags = set()
        self.running = True

    def create_board(self, rows, cols):
        """Create an empty board."""
        return [[0 for _ in range(cols)] for _ in range(rows)]

    def place_mines(self, board, mine_count):
        """Place mines randomly on the board."""
        placed_mines = 0
        while placed_mines < mine_count:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if board[row][col] != -1:
                board[row][col] = -1
                placed_mines += 1

    def update_board_numbers(self, board):
        """Update the numbers on the board based on mine proximity."""
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] == -1:
                    continue
                mine_count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < self.rows and 0 <= col + j < self.cols:
                            if board[row + i][col + j] == -1:
                                mine_count += 1
                board[row][col] = mine_count

    def print_board(self):
        """Print the current state of the visible board."""
        print("Current Board:")
        for row in self.visible_board:
            print(" ".join(str(cell) for cell in row))

    def reveal_cell(self, row, col):
        """Reveal the selected cell."""
        if self.visible_board[row][col] != "?":
            return  # Already revealed or flagged
        if self.game_board[row][col] == -1:
            self.visible_board[row][col] = "*"
        else:
            self.visible_board[row][col] = str(self.game_board[row][col])

    def check_victory(self):
        """Check if all non-mine cells are revealed."""
        for row in range(self.rows):
            for col in range(self.cols):
                if (
                    self.game_board[row][col] != -1
                    and self.visible_board[row][col] == "?"
                ):
                    return False
        return True

    def menu(self):
        """Display the main menu."""
        print("Welcome to Minesweeper!")
        print("1: Tutorial Mode")
        print("2: Easy Mode")
        print("3: Medium Mode")
        print("4: Hard Mode")
        print(
            "You can press Ctrl+C anytime to quit the game. (Windows players, it works, don't worry.)"
        )

    def init_game(self):
        self.game_board = self.create_board(self.rows, self.cols)
        self.visible_board = [["?" for _ in range(self.cols)] for _ in range(self.rows)]
        self.place_mines(self.game_board, self.mines)
        self.update_board_numbers(self.game_board)

    def play(self):
        """The main game loop."""
        while True:
            self.menu()  # Display the menu
            mode = input("Enter the number for mode (1/2/3/4): ").strip()

            if mode == "1":
                self.rows, self.cols, self.mines = 4, 4, 2
            elif mode == "2":
                self.rows, self.cols, self.mines = 10, 10, 20
            elif mode == "3":
                self.rows, self.cols, self.mines = 23, 23, 106
            elif mode == "4":
                self.rows, self.cols, self.mines = 50, 50, 500
            else:
                print("Invalid mode choice. Defaulting to Tutorial Mode.")
                self.rows, self.cols, self.mines = 4, 4, 2

            self.init_game()

            # Tutorial Mode message
            if self.rows == 4 and self.cols == 4:
                print(
                    "Welcome to Tutorial Mode! This is a small 4x4 board with only 2 mines."
                )
                print("Try to reveal all cells without stepping on a mine. Good luck!")

            # Warning message for the player
            print(
                "WARNING: The grid uses 0-based indexing. The top-left corner is (0, 0)."
            )

            while True:
                self.print_board()

                # Get player input
                user_input = input(
                    "Enter your move (e.g. R,1,2 to reveal or M,1,2 to mark): "
                ).strip()

                if user_input.lower().startswith("r"):
                    try:
                        _, row, col = user_input.split(",")
                        row, col = int(row), int(col)
                    except ValueError:
                        print("Invalid input. Please enter in the format (R,row,col).")
                        continue

                    if not (0 <= row < self.rows and 0 <= col < self.cols):
                        print("Invalid position. Try again.")
                        continue

                    if self.game_board[row][col] == -1:
                        print("Game Over! You hit a mine!")
                        self.reveal_cell(row, col)  # Reveal the mine
                        self.print_board()
                        break

                    self.reveal_cell(row, col)

                    if self.check_victory():
                        print("Congratulations! You've won!")
                        self.print_board()
                        break

                elif user_input.lower().startswith("m"):
                    try:
                        _, row, col = user_input.split(",")
                        row, col = int(row), int(col)
                    except ValueError:
                        print("Invalid input. Please enter in the format (M,row,col).")
                        continue

                    if not (0 <= row < self.rows and 0 <= col < self.cols):
                        print("Invalid position. Try again.")
                        continue

                    # Mark or unmark with 'F' as a flag
                    if (row, col) not in self.flags:
                        self.flags.add((row, col))
                        self.visible_board[row][col] = "F"  # Flag the cell
                    else:
                        self.flags.remove((row, col))
                        self.visible_board[row][col] = "?"  # Unflag the cell

                else:
                    print("Invalid input. Please use 'R' to reveal or 'M' to mark.")


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
