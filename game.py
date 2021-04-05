import pygame
from pygame.math import Vector2
import random
from board import *
from boardPiece import *
 
class Game():
    
    def __init__(self):
        pygame.init()
        self.b = Board()
        self.screen = pygame.display.set_mode((800, 600))
        
    #draws the board
    def draw(self, screen):
        cnt = 0
        for i in range(8):
            for j in range(8):
                #print(self.b.pieces[0][1].__class__.__name__)

                if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                    
                    if self.b.pieces[i][j].__class__.__name__.find('Pawn')>-1:
                        pygame.draw.rect(screen, (100, 60, 128), self.b.pieces[i][j].rect)
                    elif self.b.pieces[i][j].__class__.__name__.find('Rook')>-1:
                        pygame.draw.rect(screen, (100, 100, 128), self.b.pieces[i][j].rect)
                    elif self.b.pieces[i][j].__class__.__name__.find('Knight')>-1:   
                        pygame.draw.rect(screen, (120, 20, 128), self.b.pieces[i][j].rect)
                    elif self.b.pieces[i][j].__class__.__name__.find('Bishop')>-1:
                        pygame.draw.rect(screen, (130, 30, 128), self.b.pieces[i][j].rect)
                    elif self.b.pieces[i][j].__class__.__name__.find('Queen')>-1:
                        pygame.draw.rect(screen, (140, 40, 128), self.b.pieces[i][j].rect)
                    elif self.b.pieces[i][j].__class__.__name__.find('King')>-1:
                        pygame.draw.rect(screen, (150, 50, 128), self.b.pieces[i][j].rect)
                    else:
                        pygame.draw.rect(screen, (0, 0, 128), self.b.pieces[i][j].rect)
                else:
                    
                    if self.b.pieces[i][j].__class__.__name__.find('Pawn')>-1:
                        pygame.draw.rect(screen, (100, 60, 128), self.b.pieces[i][j].rect)
                    elif self.b.pieces[i][j].__class__.__name__.find('Rook')>-1:
                        pygame.draw.rect(screen, (100, 100, 128), self.b.pieces[i][j].rect)
                    elif self.b.pieces[i][j].__class__.__name__.find('Knight')>-1:   
                        pygame.draw.rect(screen, (120, 20, 128), self.b.pieces[i][j].rect)
                    elif self.b.pieces[i][j].__class__.__name__.find('Bishop')>-1:
                        pygame.draw.rect(screen, (130, 30, 128), self.b.pieces[i][j].rect)
                    elif self.b.pieces[i][j].__class__.__name__.find('Queen')>-1:
                        pygame.draw.rect(screen, (140, 40, 128), self.b.pieces[i][j].rect)
                    elif self.b.pieces[i][j].__class__.__name__.find('King')>-1:
                        pygame.draw.rect(screen, (150, 50, 128), self.b.pieces[i][j].rect)
                    else:
                        pygame.draw.rect(screen, (0, 128, 128), self.b.pieces[i][j].rect)
                cnt+=1

    def clickedOnPiece(self):
        x,y = pygame.mouse.get_pos()
        a=-1
        b=-1
        for i in range(8):
            for j in range(8):
                if x>0 and y>0 and 50+40*i < (x) and 50+(i+1)*40 > (x) and (y) > 50+j*40 and (y) < 50+40*(j+1) and self.b.pieces[j][i].__class__.__name__.find('Piece')==-1:
                    a=i
                    b=j
        return a,b

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if pygame.mouse.get_pressed(num_buttons=3)==(1,0,0) and self.clickedOnPiece() != (-1,-1):
            pos = self.clickedOnPiece()
            self.b.pieces[pos[1]][pos[0]].chooseMove(self.screen)
            print(self.b.test_drawBoard())

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                    running = False

                self.screen.fill((0, 0, 0))
                self.handle_keys()
                self.draw(self.screen)
                
                pygame.display.update()

                clock.tick(40)

if __name__=='__main__':
    
    
    game = Game()
    game.run()
    