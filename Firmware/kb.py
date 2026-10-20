import board                                  # Translates board."PIN" to the actual pins on the board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner

class MyKeyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()
        # Matrix setup on the board
        self.scanner = MatrixScanner(
            row_pins=[board.D6, board.D2, board.D3],
            col_pins=[board.GP4, board.GP5, board.GP6],
            diodetype=MatrixScanner.DiodeType.COL2ROW
        )