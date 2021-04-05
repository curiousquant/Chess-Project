from board import *
from piece import *
import pygame 

class BoardPiece(pygame.sprite.Sprite):
    def __init__(self,piece,rects,special):
        self.piece = piece
        self.rects = rects
        self.special = special
    
    def moveChoice(self):
        i,j = self.piece.chooseMove()
        #self.special.move_ip(i*40,j*40)
