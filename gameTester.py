from game import *
import numpy as np
if __name__=='__main__2':
    g = Game()
    board = g.b
    pieces = board.pieces

    wpawns = []
    bpawn = []
    #initialize pawns and pieces
    for i in range(2):
        for j in range(8):
            wpawns.append(pieces[i+6][j])
            bpawns.append(pieces[i][j])
    
    running=True
    turn=0
    while(running):
        if turn%2:
            pass
        else:
            pass
        turn+=1


def logicloop(N,k,output):
    if k>0:
        for i in range(N):
            print(i,k)
            output[i+k*5,k-1]=i
            logicloop(N,k-1,output)
            
output = np.zeros((120,3))
logicloop(5,3,output)
print(output)


