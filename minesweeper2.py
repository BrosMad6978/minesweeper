import random


class Minesweeper:
    def __init__(self):
        self.row_count = 4
        self.col_count = 4
        self.mine_count = 2
        self.game_board:list[list] = []
        self.visible_board = []
        self.flags = set()
        self.running = True

    def create_board(self):
        for _ in range(self.row_count):
            row = []
            for _ in range(self.col_count):
                row.append(0)
            self.game_board.append(row)

    def place_mines(self):
        """Place mines randomly on the board."""
        """TODO: Ayni yere 2 kez mayin koyma sansi var, farkli n tane yere mayin koymamiz lazim"""
        for i in range (self.mine_count):
            x = random.randint(0, self.col_count - 1)
            y = random.randint(0, self.row_count - 1)
            self.game_board[y][x] = -1

    def update_board_numbers(self, board):
        """Update the numbers on the board based on mine proximity."""
        ...

    def print_board(self):
        """Print the current state of the visible board."""
        ...

    def reveal_cell(self, row, col):
        """Reveal the selected cell."""
        ...

    def check_victory(self):
        """Check if all non-mine cells are revealed."""
        ...

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

    def play(self):
        """The main game loop."""
        ...


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
