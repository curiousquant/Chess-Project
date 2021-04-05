from piece import *
class Knight(Piece):
    def __init__(self,x,y,color,board,rect):
        super().__init__(x,y,color,board,rect)

    def move(self,x,y):
        self.board.boardarr[self.x,self.y] = 0
        self.board.boardarr[x,y] = 1

        tmpPiece = self.board.pieces[self.x][self.y]
        tmpPiece2 = self.board.pieces[x][y]
        self.board.pieces[self.x][self.y] = Piece(self.x,self.y,None,self,self.board.pieces[self.x][self.y].rect)
        self.board.pieces[x][y] = tmpPiece
        self.board.pieces[x][y].x = x
        self.board.pieces[x][y].y = y
        self.board.pieces[x][y].rect = tmpPiece2.rect    

    def calcAllPossibleMoves(self):
        multipler = 1
        if self.color == 'black':
            multipler = 1
        else:
            multipler = -1
        board = self.board.pieces
        boardarr = self.board.boardarr
        allmoves = []
        #Custom tailored to Knight behaviour
        if self.x+1*multipler>-1 and self.y-2>-1 and self.x+1*multipler<8 and self.y-2<8:
            if (board[self.x][self.y].color != board[self.x+1*multipler][self.y-2].color):
                allmoves.append([self.x+1*multipler,self.y-2])
        if self.x+1*multipler>-1 and self.y+2>-1 and self.x+1*multipler<8 and self.y+2<8:
            if (board[self.x][self.y].color != board[self.x+1*multipler][self.y+2].color):
                allmoves.append([self.x+1*multipler,self.y+2])
        if self.x-1*multipler>-1 and self.y-2>-1 and self.x-1*multipler<8 and self.y-2<8:
            if (board[self.x][self.y].color != board[self.x-1*multipler][self.y-2].color) :
                allmoves.append([self.x-1*multipler,self.y-2])
        if self.x-1*multipler>-1 and self.y+2>-1 and self.x-1*multipler<8 and self.y+2<8:
            if (board[self.x][self.y].color != board[self.x-1*multipler][self.y+2].color):
                allmoves.append([self.x-1*multipler,self.y+2])

        if self.x+2*multipler>-1 and self.y+1>-1 and self.x+2*multipler<8 and self.y+1<8:
            if (board[self.x][self.y].color != board[self.x+2*multipler][self.y+1].color):
                allmoves.append([self.x+2*multipler,self.y+1])
        if self.x+2*multipler>-1 and self.y-1>-1 and self.x+2*multipler<8 and self.y-1<8:
            if (board[self.x][self.y].color != board[self.x+2*multipler][self.y-1].color):
                allmoves.append([self.x+2*multipler,self.y-1])
        if self.x-2*multipler>-1 and self.y-1>-1 and self.x-1*multipler<8 and self.y-2<8:
            if (board[self.x][self.y].color != board[self.x-2*multipler][self.y-1].color):
                allmoves.append([self.x-2*multipler,self.y-1])
        if self.x-2*multipler>-1 and self.y+1>-1 and self.x-2*multipler<8 and self.y+1<8:
            if (board[self.x][self.y].color != board[self.x-2*multipler][self.y+1].color):
                allmoves.append([self.x-2*multipler,self.y+1])
        return allmoves
