import numpy as np

from settings import BOARD_WIDTH, BOARD_HEIGHT
from pieces import get_piece


class Tetris:

    def __init__(self):

        self.board = np.zeros(
            (BOARD_HEIGHT, BOARD_WIDTH),
            dtype=int
        )

        self.piece = get_piece()

        self.x = 3
        self.y = 0

        self.score = 0


    def collision(self):

        for row, line in enumerate(self.piece):

            for col, value in enumerate(line):

                if value:

                    nx = self.x + col
                    ny = self.y + row

                    if nx < 0 or nx >= BOARD_WIDTH:
                        return True

                    if ny >= BOARD_HEIGHT:
                        return True

                    if ny >= 0 and self.board[ny][nx]:
                        return True

        return False


    def move(self, direction):

        self.x += direction

        if self.collision():
            self.x -= direction


    def rotate(self):

        old_piece = self.piece

        self.piece = [
            list(row)
            for row in zip(*self.piece[::-1])
        ]

        if self.collision():
            self.piece = old_piece


    def drop(self):

        self.y += 1

        if self.collision():

            self.y -= 1

            self.lock_piece()

            self.clear_lines()

            self.piece = get_piece()

            self.x = 3
            self.y = 0



    def lock_piece(self):

        for row, line in enumerate(self.piece):

            for col, value in enumerate(line):

                if value:

                    self.board[
                        self.y + row,
                        self.x + col
                    ] = 1



    def clear_lines(self):

        new_board = []

        cleared = 0

        for row in self.board:

            if all(row):

                cleared += 1

            else:

                new_board.append(row)


        while len(new_board) < BOARD_HEIGHT:

            new_board.insert(
                0,
                np.zeros(BOARD_WIDTH, dtype=int)
            )


        self.board = np.array(new_board)


        self.score += cleared * 100
