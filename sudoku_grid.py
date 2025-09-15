import random
import copy

class SudokuGrid:
    # This class handles the creation, validation, and solving of Sudoku puzzles.
    # It also ensures that puzzles have a unique solution when numbers are removed.

    def __init__(self, holes=40):
        # Initialize a 9x9 grid filled with zeros
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        # Generate the puzzle immediately
        self.generate_puzzle(holes)

    def is_valid(self, num, row, col):
        # Check if 'num' can be placed at (row, col) in the current grid
        if num in self.grid[row]:
            return False  # Already in row
        if num in [self.grid[i][col] for i in range(9)]:
            return False  # Already in column

        # Check 3x3 block
        start_row, start_col = 3*(row//3), 3*(col//3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row+i][start_col+j] == num:
                    return False
        return True

    def is_valid_for_grid(self, num, row, col, grid):
        # Same as is_valid, but for a given grid (used for solver)
        if num in grid[row]:
            return False
        if num in [grid[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3*(row//3), 3*(col//3)
        for i in range(3):
            for j in range(3):
                if grid[start_row+i][start_col+j] == num:
                    return False
        return True

    def fill_grid(self):
        # Fill the grid completely using backtracking
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

    def find_all_solutions(self, grid, solutions, limit=2):
        # Find all solutions up to a limit (makes sure the puzzle is unique)
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid_for_grid(num, i, j, grid):
                            grid[i][j] = num
                            self.find_all_solutions(grid, solutions, limit)
                            grid[i][j] = 0
                    return
        # Grid is full, add a solution
        solutions.append(copy.deepcopy(grid))
        if len(solutions) >= limit:
            return

    def generate_puzzle(self, holes=40):
        # First, fill the grid completely
        self.fill_grid()

        # Now remove numbers randomly while keeping the puzzle uniquely solvable
        attempts = holes
        while attempts > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.grid[row][col] != 0:
                backup = self.grid[row][col]
                self.grid[row][col] = 0

                # Check if puzzle still has a unique solution
                grid_copy = copy.deepcopy(self.grid)
                solutions = []
                self.find_all_solutions(grid_copy, solutions)
                if len(solutions) != 1:
                    # Undo removal if uniqueness is broken
                    self.grid[row][col] = backup
                else:
                    attempts -= 1
