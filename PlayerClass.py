# python 2
#
# Homework 11, Problem 2
# Name: Domingo Gallardo Saavedra
#

class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
                
    def oppCh(self):
        if self.ox == 'X':
            return 'O'
        elif self.ox == 'O':
            return 'X'
    
    def scoreBoard(self, b):
        if b.winsFor(self.ox) and not b.winsFor(self.oppCh()):
            return 100.0
        elif b.winsFor(self.oppCh()) and not b.winsFor(self.ox):
            return 0.0
        elif not b.winsFor(self.ox) and not b.winsFor(self.oppCh()):
            return 50.0
  
    def tiebreakMove(self, scores):
        import random
        auxMax = 0
        for i in scores:
            if i >= auxMax:
                auxMax = i
        
        maxIndices = [i for i in range(len(scores)) if scores[i] == auxMax]
        if len(maxIndices) == 1:
            return maxIndices[0]
        else:
            if self.tbt == 'LEFT':
                return maxIndices[0]
            elif self.tbt == 'RIGHT':
                return maxIndices[-1]
            elif self.tbt == 'RANDOM':
                return maxIndices[random.choice(len(maxIndices))]
    
    def scoresFor(self, board):
            '''Returns a list of the scores for each column.'''
            scores = [50.0] * board.width
            for col in range(board.width):
                if board.data[0][col] != ' ':
                    scores[col] = -1.0
                elif board.winsFor(self.ox):
                    scores[col] = self.scoreBoard(board)
                elif self.ply == 0:
                    scores[col] = 50.0
                else:
                    board.addMove(col, self.ox)
                    if board.winsFor(self.ox):
                        scores[col] = self.scoreBoard(board)
                    else:
                        opponent = Player(self.oppCh(), self.tbt, self.ply -1)
                        opponentScores = opponent.scoresFor(board)
                        scores[col] = 100 - max(opponentScores)
                    board.delMove(col)
            return scores

    def nextMove(self, board):
        '''Returns the integer for the next move as determined by scoresFor.'''
        scores = self.scoresFor(board)
        return self.tiebreakMove(scores)
        
    def playGame(self, playerX, playerO):
                '''Used to host a two player game of connect four with one or two of those players being humans.'''
                print("Welcome to Connect Four!")
                counter = 0
                while True:     #Game play
                        print()      #Add some space between moves
                        print(self)
                        print()     #Add some more white space
                        while counter % 2 == 0:
                                if playerX == 'human':
                                    choice = int(input("X's choice:    "))
                                    if self.isMoveLegal(choice) == True:
                                        self.addMove(choice, 'X')
                                        break
                                    else:
                                        print("Invalid move, try again.")
                                else:
                                    self.addMove(int(playerX.nextMove(self)), 'X')
                                    break
                        while counter % 2 == 1:
                                if playerO == 'human':
                                    choice = int(input("O's choice:    "))
                                    if self.isMoveLegal(choice) == True:
                                        self.addMove(choice, 'O')
                                        break
                                    else:
                                        print("Invalid move, try again.")
                                else:
                                    self.addMove(int(playerO.nextMove(self)), 'O')
                                    break

                        if self.isWinFor('X') == True:
                                print(self)
                                print("X Wins!")
                                return
                        elif self.isWinFor('O') == True:
                                print(self)
                                print("O Wins!")
                                return
                        elif self.isFull == True:
                                print(self)
                                print("Board is full, no winner.")
                                return
                        counter += 1   
                
          
        
        
        

class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        
        s += '\n'
        for i in range(W):
            s += ' ' + str(i%10)
        
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        for i in range(self.height-1,-1,-1):
            if self.data[i][col] == ' ':
                self.data[i][col] = ox
                break
                
    def clear( self ):
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]
        
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'    
   
    def allowsMove(self, c):
        if c >= self.width:
            return False
        elif self.data[0][c] != ' ':
            return False
        elif c < 0:
            return False
        else:
            return True
          
    def isFull(self):
        aux = True
        for i in range(self.width):
            if self.data[0][i] == ' ':
                aux *= False
        if aux == 1:
            return True
        else:
            return False
                
    def delMove(self, c):
        for i in range(self.height):
            if self.data[i][c] != ' ':
                self.data[i][c] = ' '
                break
                
    def winsFor(self, ox):
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        win = False
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row][col+1] == ox and \
                   D[row][col+2] == ox and \
                   D[row][col+3] == ox:
                    win = True
                    
        # check for vertical wins
        for row in range(0,H-3):
            for col in range(0,W):
                if D[row][col] == ox and \
                   D[row+1][col] == ox and \
                   D[row+2][col] == ox and \
                   D[row+3][col] == ox:
                    win = True
                    
        # check for diagonal "\" wins
        for row in range(0,H-3):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row+1][col+1] == ox and \
                   D[row+2][col+2] == ox and \
                   D[row+3][col+3] == ox:
                    win = True
                    
        # check for diagonal "/" wins
        for row in range(0,H-3):
            for col in range(3,W):
                if D[row][col] == ox and \
                   D[row+1][col-1] == ox and \
                   D[row+2][col-2] == ox and \
                   D[row+3][col-3] == ox:
                    win = True
        return win
        
        
    def hostGame(self):
        print "Welcome to Connect Four!"
        while True:
            print
            print self
            users_col = -1
            
            while self.allowsMove( users_col ) == False:
                users_col = input("X Choose a column: ")
            self.addMove(users_col, 'X')
            if self.winsFor('X'):
                win = 'X'
                break
            elif self.isFull():
                win = 'Tie'
                break
                
            print
            print self
            
            users_col = -1
            
            while self.allowsMove( users_col ) == False:
                users_col = input("O Choose a column: ")
            self.addMove(users_col, 'O')
            if self.winsFor('O'):
                win = 'O'
                break
            elif self.isFull():
                win = 'Tie'
                break
                
        print win, "wins-Congratulations!"
        
        
        
        
        
        
        
        
        
        
        