class SudokuGame:
    """CLI interaction."""

    def __init__(self, sudoku_grid):
        self.sudoku_grid = sudoku_grid

    def print_grid(self):
        for i, row in enumerate(self.sudoku_grid.grid):
            row_str = ""
            for j, num in enumerate(row):
                row_str += str(num) if num != 0 else "."
                if (j+1)%3 == 0 and j<8:
                    row_str += " | "
                else:
                    row_str += " "
            print(row_str)
            if (i+1)%3 == 0 and i<8:
                print("-"*21)

    def play_cli(self):
        while True:
            self.print_grid()
            user_input = input("Enter row(1-9) col(1-9) num(1-9) or 'q' to quit: ")
            if user_input.lower() == 'q':
                print("Exiting game.")
                break
            try:
                row, col, num = map(int, user_input.split())
                row -= 1
                col -= 1
                if self.sudoku_grid.grid[row][col] != 0:
                    print("Cell already filled.")
                    continue
                if num < 1 or num > 9:
                    print("Number must be 1-9.")
                    continue
                if not self.sudoku_grid.is_valid(num, row, col):
                    print("Invalid move!")
                    continue
                self.sudoku_grid.grid[row][col] = num
            except:
                print("Invalid input. Format: row col num")
