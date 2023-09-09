import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        # Initialize the main window
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        # Initialize game variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # Create a 3x3 grid of buttons for the game board
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.window,
                    text="",
                    font=("Helvetica", 24),
                    width=8,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        # Check if the selected cell is empty and the game is not over
        if self.board[row][col] == "" and not self.check_winner():
            # Update the board with the current player's symbol
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Switch to the other player's turn
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

            # Check if there is a winner or a tie
            winner = self.check_winner()
            if winner:
                # Display a message box with the winner's name
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_board()
            elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
                # If the board is full and there's no winner, it's a tie
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        return ""

    def reset_board(self):
        # Reset the board and switch to player X's turn
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"

    def run(self):
        # Start the Tkinter main loop
        self.window.mainloop()

if __name__ == "__main__":
    # Create and run the Tic-Tac-Toe game
    game = TicTacToe()
    game.run()
