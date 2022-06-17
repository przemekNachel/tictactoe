import msvcrt


from board import Board
from view import View


class Game:

    def __init__(self):
        self.board = Board()

    @staticmethod
    def getch():
        return str(msvcrt.getch())[-2]

    def game(self):
        while True:
            View.print_interface(self.board, self.board.winner)
            if self.board.winner or self.board.end:
                break
            choice = Game.getch()
            if choice == "0":
                break
            if choice.isdigit():
                self.board.fill_field(choice)


Game().game()
