from piece import *
class King(Piece):

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
        deltax = 2
        deltay = 2
        if self.color == 'black':
            multipler = 1
        else:
            multipler = -1

        board = self.board.pieces
        boardarr = self.board.boardarr
        allmoves = []


        sumUp = 0
        sumDown = 0
        sumLeft = 0
        sumRight = 0
        #moving up
        for i in range(0,2):
            if sumDown <2:
                if self.x-i*multipler>-1 and self.x-i*multipler<8:
                    allmoves.append([self.x-i*multipler,self.y])
                    sumDown += boardarr[self.x-i*multipler,self.y]
            elif sumDown==2:
                break
        
        #moving down
        for i in range(0,deltax):
            if sumUp <2:
                if self.x+i*multipler>-1 and self.x+i*multipler<8:
                    allmoves.append([self.x+i*multipler,self.y])
                    sumUp += boardarr[self.x+i*multipler,self.y]
            elif sumUp==2:
                break

        #moving left
        for i in range(0,2):
            if sumLeft <2:
                if self.y-i*multipler>-1 and self.y-i*multipler<8:
                    allmoves.append([self.x,self.y-i*multipler])
                    sumLeft += boardarr[self.x,self.y-i*multipler]
            elif sumLeft==2:
                break

        #moving right
        for i in range(0,deltay):
            if sumRight <2:
                if self.y+i*multipler>-1 and self.y-i*multipler<8:
                    allmoves.append([self.x,self.y+i*multipler])
                    sumRight += boardarr[self.x,self.y+i*multipler]
            elif sumRight==2:
                break      
              
        sumUp = 0
        sumDown = 0
        sumLeft = 0
        sumRight = 0

        #moving upleft
        for i in range(0,2):
            if sumDown <2 and self.x-i*multipler>-1 and self.y-i*multipler>-1 and self.x-i*multipler<8 and self.y-i*multipler<8:
                allmoves.append([self.x-i*multipler,self.y-i*multipler])
                sumDown += boardarr[self.x-i*multipler,self.y-i*multipler]
            elif sumDown==2:
                break
        
        #moving downright
        for i in range(0,deltax):
            if sumUp <2 and self.x+i*multipler>-1 and self.y+i*multipler>-1  and self.x+i*multipler<8 and self.y+i*multipler<8:
                allmoves.append([self.x+i*multipler,self.y+i*multipler])
                sumUp += boardarr[self.x+i*multipler,self.y+i*multipler]
            elif sumUp==2:
                break

        #moving leftdown
        for i in range(0,2):
            if sumLeft <2 and self.x+i*multipler>-1 and self.y-i*multipler>-1 and self.x+i*multipler<8 and self.y-i*multipler<8:
                allmoves.append([self.x+i*multipler,self.y-i*multipler])
                sumLeft += boardarr[self.x+i*multipler,self.y-i*multipler]
            elif sumLeft==2:
                break

        #moving rightup
        for i in range(0,deltay):
            if sumRight <2 and self.x-i*multipler>-1 and self.y+i*multipler>-1 and self.x-i*multipler<8 and self.y+i*multipler<8:
                allmoves.append([self.x-i*multipler,self.y+i*multipler])
                sumRight += boardarr[self.x-i*multipler,self.y+i*multipler]
            elif sumRight==2:
                break        

        return allmoves
        
