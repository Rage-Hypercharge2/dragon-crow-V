import numpy as np
from settings import *
from pieces import get_piece


class Tetris:

    def __init__(self):

        self.board=np.zeros(
            (BOARD_HEIGHT,BOARD_WIDTH),
            dtype=int
        )

        self.piece=get_piece()

        self.x=3
        self.y=0

        self.score=0



    def collision(self):

        for r,row in enumerate(self.piece):

            for c,value in enumerate(row):

                if value:

                    nx=self.x+c
                    ny=self.y+r

                    if (
                        nx<0 or
                        nx>=BOARD_WIDTH or
                        ny>=BOARD_HEIGHT
                    ):
                        return True

                    if ny>=0 and self.board[ny][nx]:
                        return True

        return False



    def move(self,dx):

        self.x+=dx

        if self.collision():
            self.x-=dx



    def rotate(self):

        old=self.piece

        self.piece=[
            list(row)
            for row in zip(*self.piece[::-1])
        ]

        if self.collision():
            self.piece=old



    def drop(self):

        self.y+=1

        if self.collision():

            self.y-=1
            self.lock()

            self.clear()

            self.piece=get_piece()

            self.x=3
            self.y=0



    def lock(self):

        for r,row in enumerate(self.piece):

            for c,value in enumerate(row):

                if value:

                    self.board[
                        self.y+r,
                        self.x+c
                    ]=1



    def clear(self):

        lines=[]

        for i,row in enumerate(self.board):

            if all(row):
                lines.append(i)


        for i in lines:

            self.board=np.delete(
                self.board,
                i,
                axis=0
            )

            self.board=np.vstack(
                [
                    np.zeros(
                        (1,BOARD_WIDTH),
                        dtype=int
                    ),
                    self.board
                ]
            )

            self.score+=100
