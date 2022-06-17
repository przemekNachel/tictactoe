import os


class View:

    BOARD_TEMPLATE = "{f1}|{f2}|{f3}\n---+---+---\n{f4}|{f5}|{f6}\n---+---+---\n{f7}|{f8}|{f9}\n"
    CIRCLE = " O "
    CROSS = " X "
    EMPTY = "   "
    INTERFACE = "{status}\n\n{board}\n\n{menu}"
    MENU = "1-9 Fill field\n0. Exit"

    @staticmethod
    def get_player_name(is_circle):
        if is_circle:
            if is_circle == " X ":
                return "Cross"
            return "Circle"
        else:
            return "Cross"

    @staticmethod
    def print_interface(board, status=EMPTY, menu=EMPTY):
        os.system('cls' if os.name == 'nt' else 'clear')
        if status:
            status = "{} Won!".format(View.get_player_name(board.winner))
        else:
            status = "Player: {}".format(View.get_player_name(board.is_circle_turn))
            menu = View.MENU
        print(View.INTERFACE.format(status=status,
                                    board=board.get_board(),
                                    menu=menu))
