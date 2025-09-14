import matplotlib.pyplot as plt

class SudokuDisplay:
    """Matplotlib interactive visualization with clickable and typeable cells."""

    def __init__(self, sudoku_grid):
        self.sudoku_grid = sudoku_grid
        self.selected_cell = None  # Track which cell is selected
        self.fig, self.ax = plt.subplots(figsize=(6,6))
        self.draw_grid()

        # Connect events
        self.cid_click = self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.cid_key = self.fig.canvas.mpl_connect('key_press_event', self.on_key)

        plt.show(block=False)

    def draw_grid(self):
        """Draw the Sudoku grid and numbers."""
        self.ax.clear()
        for i in range(10):
            lw = 2 if i % 3 == 0 else 1
            self.ax.plot([0,9],[i,i],'k',lw=lw)
            self.ax.plot([i,i],[0,9],'k',lw=lw)

        # Highlight selected cell
        if self.selected_cell:
            row, col = self.selected_cell
            self.ax.add_patch(
                plt.Rectangle((col, 8-row), 1, 1, fill=False, edgecolor='red', lw=3)
            )

        # Draw numbers
        for i in range(9):
            for j in range(9):
                num = self.sudoku_grid.grid[i][j]
                if num != 0:
                    self.ax.text(j+0.5, 8.5-i, str(num), fontsize=16,
                                 ha='center', va='center')
        self.ax.set_xlim(0,9)
        self.ax.set_ylim(0,9)
        self.ax.axis('off')
        self.fig.canvas.draw_idle()

    def on_click(self, event):
        """Select the clicked cell."""
        if event.inaxes != self.ax:
            return
        col = int(event.xdata)
        row = int(8 - event.ydata)
        self.selected_cell = (row, col)
        self.draw_grid()

    def on_key(self, event):
        """Handle key press to fill selected cell."""
        if not self.selected_cell:
            return
        row, col = self.selected_cell
        if self.sudoku_grid.grid[row][col] != 0:
            print(f"Cell ({row+1},{col+1}) already filled!")
            return

        if event.key.isdigit() and 1 <= int(event.key) <= 9:
            num = int(event.key)
            if self.sudoku_grid.is_valid(num, row, col):
                self.sudoku_grid.grid[row][col] = num
                self.draw_grid()
            else:
                print("Invalid move!")
        elif event.key.lower() == 'backspace':
            self.sudoku_grid.grid[row][col] = 0
            self.draw_grid()
