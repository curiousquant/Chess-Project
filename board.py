from array import *
from piece import * 
from pawn import *
from rook import *
from bishop import *
from queen import *
from king import *
from knight import *

import pygame
import numpy as np

class Board():

    def __init__(self):
        cubeWidth = 40
        cubeHeight = 40
        self.pieces = [[Piece(i,j,None,self,
        pygame.rect.Rect(50+cubeWidth*i,50+cubeHeight*j,cubeWidth,cubeHeight)) for i in range(8)] for j in range(8)]
        #fill in rest of the board
        
        for i in range(8):
            
            self.pieces[1][i] = Pawn(1,i,'black',self,self.pieces[1][i].rect)
            self.pieces[6][i] = Pawn(6,i,'white',self,self.pieces[6][i].rect)
        
        self.pieces[0][0] = Rook(0,0,'black',self,self.pieces[0][0].rect)
        self.pieces[0][1] = Knight(0,1,'black',self,self.pieces[0][1].rect)
        self.pieces[0][2] = Bishop(0,2,'black',self,self.pieces[0][2].rect)
        self.pieces[0][3] = King(0,3,'black',self,self.pieces[0][3].rect)
        self.pieces[0][4] = Queen(0,4,'black',self,self.pieces[0][4].rect)
        self.pieces[0][5] = Bishop(0,5,'black',self,self.pieces[0][5].rect)
        self.pieces[0][6] = Knight(0,6,'black',self,self.pieces[0][6].rect)
        self.pieces[0][7] = Rook(0,7,'black',self,self.pieces[0][7].rect)
        
        self.pieces[7][0] = Rook(7,0,'white',self,self.pieces[7][0].rect)
        self.pieces[7][1] = Knight(7,1,'white',self,self.pieces[7][1].rect)
        self.pieces[7][2] = Bishop(7,2,'white',self,self.pieces[7][2].rect)
        self.pieces[7][3] = Queen(7,3,'white',self,self.pieces[7][3].rect)
        self.pieces[7][4] = King(7,4,'white',self,self.pieces[7][4].rect)
        self.pieces[7][5] = Bishop(7,5,'white',self,self.pieces[7][5].rect)
        self.pieces[7][6] = Knight(7,6,'white',self,self.pieces[7][6].rect)
        self.pieces[7][7] = Rook(7,7,'white',self,self.pieces[7][7].rect)
        
        self.boardarr = np.zeros([8,8])
        self.boardarr[0:2,:]=1
        self.boardarr[6:8,:]=1

        #self.pieces[1][1].chooseMove()
    def test_drawBoard(self):
        for i in range(8):
            print(self.pieces[i][0].__class__.__name__,self.pieces[i][1].__class__.__name__,
            self.pieces[i][2].__class__.__name__,self.pieces[i][3].__class__.__name__,
            self.pieces[i][4].__class__.__name__,self.pieces[i][5].__class__.__name__,
            self.pieces[i][6].__class__.__name__,self.pieces[i][7].__class__.__name__)    
    def test_drawBoard2(self):
        for i in range(8):
            print(self.pieces[i][0].rect.center,self.pieces[i][1].rect.center,
            self.pieces[i][2].rect.center,self.pieces[i][3].rect.center,
            self.pieces[i][4].rect.center,self.pieces[i][5].rect.center,
            self.pieces[i][6].rect.center,self.pieces[i][7].rect.center)    
if __name__=='__main__':
    b = Board()
    print(b.boardarr)
    b.pieces[1][1].chooseMove()
