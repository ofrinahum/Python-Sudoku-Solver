from sudoku_grid import SudokuGrid
from sudoku_display import SudokuDisplay
from sudoku_game import SudokuGame

def main():
    grid = SudokuGrid(holes=40)
    display = SudokuDisplay(grid)  # fully interactive GUI
    print("Click a cell and type a number (1-9) or Backspace to clear.")

    # Optional: still keep CLI for reference
    game = SudokuGame(grid)
    game.play_cli()

if __name__ == "__main__":
    main()
