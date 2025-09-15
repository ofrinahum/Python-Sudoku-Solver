import matplotlib.pyplot as plt
from sudoku_grid import SudokuGrid
from sudoku_display import SudokuDisplay

class DifficultyMenu:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.levels = {"Easy": 30, "Medium": 40, "Hard": 55}
        self.draw_menu()
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        plt.show()

    def draw_menu(self):
        self.ax.clear()

        # Title
        self.ax.text(
            4.5, 7.5, "Choose Difficulty",
            ha="center", va="center",
            fontsize=22, fontweight="bold", family="serif", color="#4B0082"
        )

        # Pastel button colors
        colors = ["#AEC6CF", "#CBAACB", "#FFB347"]  # pastel blue, purple, orange

        for i, (level, _) in enumerate(self.levels.items()):
            self.ax.add_patch(
                plt.Rectangle(
                    (3, 5 - i*1.5), 3, 1,
                    color=colors[i], alpha=0.7,
                    ec="black", lw=2
                )
            )
            self.ax.text(
                4.5, 5.5 - i*1.5, level,
                ha="center", va="center",
                fontsize=16, fontweight="bold", family="serif", color="black"
            )

        self.ax.set_xlim(0, 9)
        self.ax.set_ylim(0, 9)
        self.ax.axis("off")
        self.fig.canvas.draw_idle()

    def on_click(self, event):
        # Handle click to select difficulty
        for i, (level, holes) in enumerate(self.levels.items()):
            if 3 <= event.xdata <= 6 and (5 - i*1.5) <= event.ydata <= (6 - i*1.5):
                plt.close(self.fig)
                sudoku = SudokuGrid(holes)
                SudokuDisplay(sudoku)
