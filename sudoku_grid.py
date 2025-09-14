import random

class SudokuGrid:
    """Handles puzzle creation, validation, and solving."""

    def __init__(self, holes=40):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.generate_puzzle(holes)

    def is_valid(self, num, row, col):
        if num in self.grid[row]:
            return False
        if num in [self.grid[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3*(row//3), 3*(col//3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row+i][start_col+j] == num:
                    return False
        return True

    def fill_grid(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.is_valid(num, row, col):
                            self.grid[row][col] = num
                            if self.fill_grid():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True

    def generate_puzzle(self, holes=40):
        self.fill_grid()
        count = 0
        while count < holes:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.grid[row][col] != 0:
                self.grid[row][col] = 0
                count += 1
