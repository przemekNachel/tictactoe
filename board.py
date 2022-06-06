class Board:

    BOARD_TEMPLATE = "{f1}|{f2}|{f3}\n-----------\n{f4}|{f5}|{f6}\n-----------\n{f7}|{f8}|{f9}\n"

    def __init__(self):
        self.fields = {
            "f1": "   ", "f2": "   ", "f3": "   ",
            "f4": "   ", "f5": "   ", "f6": "   ",
            "f7": "   ", "f8": "   ", "f9": "   "}

    def get_board(self):
        return Board.BOARD_TEMPLATE.format(**self.fields)

    def fill_field(self, sign, field):
        self.fields["f" + str(field)] = sign
