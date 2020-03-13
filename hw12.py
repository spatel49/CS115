'''
Created on December 5, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Siddhanth Patel
username: spate144

CS115 - Hw 8
'''
from life_starter.csgrid import ROW

class Board(object):
    def __init__(self, width=7, height=6):
        self.width = int(width)
        self.height = int(height)
        self.board = self.creates_board()
    
    def creates_row(self):
        row = []
        for i in range(self.width):
            row += ['']
        return row
    
    def creates_board(self):
        board = []
        for i in range(self.height):
            board += [self.creates_row()]
        return board
    
    def allowsMove(self, col):
        """It returns True if the calling Board object can allow a move into column c (because there is space available).
        It returns False if c does not have space available or if it is not a valid column."""
        try:
            int(col)
        except:
            return False
        col = int(col)
        if col < self.width:
            if self.board[0][col] == "":
                return True
            return False
        return False
        
    def addMove(self, col, ox):
        """"This method should add an ox checker, where ox is a variable holding a string that is either "X" or "O", into column col."""
        row = 0
        if self.allowsMove(col) == True:
            for x in range(self.height):
                if self.board[x][col] == "":
                    row += 1
            self.board[row-1][col] = ox
            
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
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            nextCh = ''
                
    def delMove(self, col):
        """It removes the top checker from the column col. If the column is empty, then delMove should do nothing."""
        if self.board[self.height - 1][col] != "":
            count = 0
            while count < self.height:
                if self.board[count][col] == "":
                    count += 1
                self.board[count][col] = ""
            
    def winsFor(self, ox):
        """This method should return True if the given checker, 'X' or 'O', held in ox, has won the calling Board. It should return False otherwise."""
        #horizontal:
        for row in range(self.height):
            count = 0
            for col in range(self.width):
                if self.board[row][col] == ox:
                    count +=1
                    if count >= 4:
                        return True
                else:
                    count = 0
        #vertical:
        for col in range(self.width):
            count = 0
            for row in range(self.height):
                if self.board[row][col] == ox:
                    count +=1
                    if count >= 4:
                        return True
                else:
                    count = 0
        
        #diagonal 1
        for row in range(self.height):
            column = 0
            r = row
            count = 0
            while column < self.width:
                if self.board[r][column] == ox:
                    count += 1
                    if count >= 4:
                        return True
                    column += 1
                    r -= 1
                else:
                    count = 0
                    column += 1
                    r -= 1
                    
        #diagonal 2
        for x in range(self.width):
            col = x
            row = self.height - 1
            count = 0
            while col < self.width and row > -1:
                if self.board[row][col] == ox:
                    count += 1
                    if count >= 4:
                        return True
                    else:
                        col -= 1
                        row -= 1
                else:
                    count = 0
                    col -= 1
                    row -= 1
    
    def __str__(self):
        """Returns the connect four board (displays the board)"""
        horizontal = "-" + "-" * 2 * self.width
        cols = ""
        for x in range(self.width):
            cols += " " + str(x)
        board = ''
        for row in range(self.height):
            board += "\n"
            for col in range(self.width):
                if self.board[row][col] == "":
                    board += "| "
                else:
                    board += ("|" + self.board[row][col])
            board += "|"
                    
        return board + "\n" + horizontal + "\n" + cols
                
            
    def hostGame(self):
        """This is a method that, when called from a connect four board object, will run a loop allowing the user(s) to play a game."""
        print("Welcome to Connect Four!\n")
        while True:
            print(self, '\n')
            X = input("Player X, please enter your column choice.\n")
            while True:
            #X's turn
                if self.allowsMove(X) == True:
                    print("X's choice: " + X + "\n")
                    self.addMove(int(X), "X")
                    print(self, '\n')
                    break
                else:
                    X = input(X + " is invalid." + " Please enter a valid column number.\n")
                    
            if self.winsFor("X") == True:
                print("X wins -- Congratulations!")
                break
            
            #O's Turn
            O = input("O player enter your column choice.\n")
            while True:
                if self.allowsMove(O) == True:
                    print("O's choice: " + O)
                    self.addMove(int(O), "O")
                    print(self, "\n")
                    break
                else:
                    O = input(O + " is invalid." + " Please enter a valid column number.\n")
            
            if self.winsFor("O") == True:
                print("O wins -- Congratulations!")
                break
            
if __name__ == "__main__":

    b = Board()
    b.hostGame()