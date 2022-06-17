from view import View


class Board:

    WIN_PATTERNS = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]

    def __init__(self):
        self.fields = {
            "f1": "   ", "f2": "   ", "f3": "   ",
            "f4": "   ", "f5": "   ", "f6": "   ",
            "f7": "   ", "f8": "   ", "f9": "   "}
        self.is_circle_turn = True
        self.winner = None
        self.end = False

    def get_board(self):
        return View.BOARD_TEMPLATE.format(**self.fields)

    def invert_sign(self):
        self.is_circle_turn = not self.is_circle_turn

    def get_sign(self):
        if self.is_circle_turn:
            return View.CIRCLE
        else:
            return View.CROSS

    def get_field(self, number):
        return self.fields["f" + str(number)]

    def set_field(self, number, value):
        self.fields["f" + str(number)] = value

    def fill_field(self, number):
        if self.get_field(number) == View.EMPTY:
            self.set_field(number, self.get_sign())
            self.check_winner()
            self.invert_sign()

    def check_line_equal(self, first, second, third):
        return self.get_field(first) == self.get_field(second) == self.get_field(third)

    def check_winner(self):
        if View.EMPTY not in self.fields.values():
            self.end = True
            return
        for pattern in Board.WIN_PATTERNS:
            if self.get_field(pattern[1]) != View.EMPTY and self.check_line_equal(*pattern):
                self.winner = self.get_field(pattern[1])







