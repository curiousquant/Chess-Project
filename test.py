
fix bounds of movement for queen and anything else - test >8


create image of board

tie each tile to a piece

for special tiles i.e. pawn, rook etc,  draw something more







board class
    64 piece objects
    initializeBoard()
        create 16 white and black pieces
    create 2 empty numpy array for logic
    white pieces: 1 for white 1 for black 0 for empty
    
piece class (board)
    color
    x
    y
    type class
        pawn
            str typename
            move()
                change x,y coordinate
                edit numpy array 

            calcAllPossibleMoves()
                using super.x, super.y, typename, board, numpy array

                regarding numpy array  

                    start at coordinates indicated by super.x, super.y
                    increment up as defined by piece type,
                        sum one at a time and hope they add to 2, then end loop
                    
                    same thing as above but increment down,left,right

                return all x,y positions 

            calcPossibleMoves()       
                dict of moves = calcAllPossibleMoves()
                loop through dict of moves
                    loop through piece in board
                        check if x,y position not occupied 
                            if it is not, add to temp dict
                        else if x,y position occupied by other color
                        if it is add to temp dict
                        
                        
                return temp dict

            chooseMove()
                select from calcPossibleMoves()
                loop through piece in board
                    if overlapping x,y of different color
                        delete board instance of opposite color piece
                move(selection)
            