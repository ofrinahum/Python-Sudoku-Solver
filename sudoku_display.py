import matplotlib.pyplot as plt

class SudokuDisplay:
    # Interactive Sudoku grid with arrow-key navigation and red invalid numbers.

    def __init__(self, sudoku_grid):
        self.sudoku_grid = sudoku_grid
        self.selected_cell = (0, 0)      # start at top-left
        self.invalid_cells = set()        # tracks cells with invalid numbers
        self.fig, self.ax = plt.subplots(figsize=(6,6))
        self.draw_grid()
        self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        plt.show()

    def draw_grid(self):
        # Draw the grid, highlights, and numbers (red if invalid)
        self.ax.clear()

        # Draw grid lines (3x3 blocks)
        for i in range(10):
            lw = 2 if i % 3 == 0 else 1
            self.ax.plot([0,9],[i,i],'k',lw=lw)
            self.ax.plot([i,i],[0,9],'k',lw=lw)

        row, col = self.selected_cell

        # Highlight row, column, block, and selected cell
        self.ax.add_patch(plt.Rectangle((0,8-row), 9,1, fill=True, color='lightblue', alpha=0.2))  # row
        self.ax.add_patch(plt.Rectangle((col,0), 1,9, fill=True, color='lightblue', alpha=0.2))    # column
        block_row, block_col = 3*(row//3), 3*(col//3)
        self.ax.add_patch(plt.Rectangle((block_col,8-block_row-2),3,3, fill=True, color='lightgreen', alpha=0.2))  # block
        self.ax.add_patch(plt.Rectangle((col,8-row),1,1, fill=False, edgecolor='red', lw=3))  # selected cell

        # Draw numbers
        for i in range(9):
            for j in range(9):
                num = self.sudoku_grid.grid[i][j]
                if num != 0:
                    # Color red if the cell is invalid
                    color = 'red' if (i,j) in self.invalid_cells else 'black'
                    self.ax.text(j+0.5, 8.5-i, str(num), fontsize=16, ha='center', va='center', color=color)

        self.ax.set_xlim(0,9)
        self.ax.set_ylim(0,9)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.fig.canvas.draw_idle()

    def on_key(self, event):
        # Handles arrow keys and number input
        row, col = self.selected_cell

        # Move selection
        if event.key == 'up':
            row = (row - 1) % 9
        elif event.key == 'down':
            row = (row + 1) % 9
        elif event.key == 'left':
            col = (col - 1) % 9
        elif event.key == 'right':
            col = (col + 1) % 9

        # Fill number
        elif event.key.isdigit() and 1 <= int(event.key) <= 9:
            num = int(event.key)
            if self.sudoku_grid.is_valid(num, row, col):
                self.sudoku_grid.grid[row][col] = num
                if (row, col) in self.invalid_cells:
                    self.invalid_cells.remove((row, col))
            else:
                self.invalid_cells.add((row, col))
                self.sudoku_grid.grid[row][col] = num

        # Clear cell
        elif event.key.lower() == 'backspace':
            self.sudoku_grid.grid[row][col] = 0
            if (row, col) in self.invalid_cells:
                self.invalid_cells.remove((row, col))

        self.selected_cell = (row, col)
        self.draw_grid()
