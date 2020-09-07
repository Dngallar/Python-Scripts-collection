# python 2
#
# Homework 10, Problem 2
# Name: Domingo Gallardo Saavedra
#

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
        
            
           
            
             
              
                
        
        