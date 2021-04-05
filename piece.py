import pygame
import time 
class Piece():
    def __init__(self,x,y,color,board,rect):
        self.color = color
        self.x = x
        self.y = y
        self.board = board
        self.rect = rect
    
    def calcAllPossibleMoves(self):
        pass

    def calcPossibleMoves(self):
        #print(self.board)
        board = self.board.pieces
        #print(board)
        allmoves = self.calcAllPossibleMoves()
        filteredMoves = []
        for i in allmoves:
            if self.color!=board[i[0]][i[1]].color:
                filteredMoves.append(i)
            
        return filteredMoves

    def clickedOnPiece(self):
        x,y = pygame.mouse.get_pos()
        a=-1
        b=-1
        for i in range(8):
            for j in range(8):
                if x>0 and y>0 and 50+40*i < (x) and 50+(i+1)*40 > (x) and (y) > 50+j*40 and (y) < 50+40*(j+1):
                    a=i
                    b=j
        return a,b

    def chooseMove(self,screen):
        filteredMoves = self.calcPossibleMoves()
        pygame.event.wait()
        running=True
        rects = []
        self.draw(screen)
        for i in filteredMoves:
            rects.append(self.board.pieces[i[0]][i[1]].rect)
            
            pygame.draw.rect(screen, (70, 70, 70), self.board.pieces[i[0]][i[1]].rect)
        pygame.display.update(rects)
            
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                    running = False
                if pygame.mouse.get_pressed(num_buttons=3)==(1,0,0): 
                    if  self.clickedOnPiece() != (-1,-1) and [self.clickedOnPiece()[1],self.clickedOnPiece()[0]] in filteredMoves:
                        self.move(self.clickedOnPiece()[1],self.clickedOnPiece()[0])
                        running=False
                    elif len(filteredMoves)==0:
                        running=False
        #return filteredMoves[choiceNum][0],filteredMoves[choiceNum][1]
        print(self.board.boardarr)
        #\print(self.board.pieces)
        #else:
            
            #return back to player's turn
    def draw(self, screen):
        cnt = 0
        for i in range(8):
            for j in range(8):
                #print(self.board.pieces[0][1].__class__.__name__)

                if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                    
                    if self.board.pieces[i][j].__class__.__name__.find('Pawn')>-1:
                        pygame.draw.rect(screen, (100, 60, 128), self.board.pieces[i][j].rect)
                    elif self.board.pieces[i][j].__class__.__name__.find('Rook')>-1:
                        pygame.draw.rect(screen, (100, 100, 128), self.board.pieces[i][j].rect)
                    elif self.board.pieces[i][j].__class__.__name__.find('Knight')>-1:   
                        pygame.draw.rect(screen, (120, 20, 128), self.board.pieces[i][j].rect)
                    elif self.board.pieces[i][j].__class__.__name__.find('Bishop')>-1:
                        pygame.draw.rect(screen, (130, 30, 128), self.board.pieces[i][j].rect)
                    elif self.board.pieces[i][j].__class__.__name__.find('Queen')>-1:
                        pygame.draw.rect(screen, (140, 40, 128), self.board.pieces[i][j].rect)
                    elif self.board.pieces[i][j].__class__.__name__.find('King')>-1:
                        pygame.draw.rect(screen, (150, 50, 128), self.board.pieces[i][j].rect)
                    else:
                        pygame.draw.rect(screen, (0, 0, 128), self.board.pieces[i][j].rect)
                else:
                    
                    if self.board.pieces[i][j].__class__.__name__.find('Pawn')>-1:
                        pygame.draw.rect(screen, (100, 60, 128), self.board.pieces[i][j].rect)
                    elif self.board.pieces[i][j].__class__.__name__.find('Rook')>-1:
                        pygame.draw.rect(screen, (100, 100, 128), self.board.pieces[i][j].rect)
                    elif self.board.pieces[i][j].__class__.__name__.find('Knight')>-1:   
                        pygame.draw.rect(screen, (120, 20, 128), self.board.pieces[i][j].rect)
                    elif self.board.pieces[i][j].__class__.__name__.find('Bishop')>-1:
                        pygame.draw.rect(screen, (130, 30, 128), self.board.pieces[i][j].rect)
                    elif self.board.pieces[i][j].__class__.__name__.find('Queen')>-1:
                        pygame.draw.rect(screen, (140, 40, 128), self.board.pieces[i][j].rect)
                    elif self.board.pieces[i][j].__class__.__name__.find('King')>-1:
                        pygame.draw.rect(screen, (150, 50, 128), self.board.pieces[i][j].rect)
                    else:
                        pygame.draw.rect(screen, (0, 128, 128), self.board.pieces[i][j].rect)
                cnt+=1
    