class CharacterBoard:
    # how many id's there are
    characterBoard_id = 0

    def __init__(self, character, board, position):
        characterBoard_id += 1
        self.characterBoard_id = characterBoard_id
        self.char
        self.character = character
        self.board = board
        self.position = position

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y
    # need to protect whether you are inbounds; perhaps leave it up to the board to deal with this

    # def moveUp(self, n):
    #     self.x -= n

    # def moveDown(self, n):
    #     self.x -= n
   
    # def moveLeft(self, n):
    #     self.x -= 1
        
    # def moveRight(self, n):
    #     self.x -= 1 





class CharacterBoardContainer: 
    def __init__(self):
        self.characters = []

    def addChar(self, characterBoard):
        self.characters.append(characterBoard)
    


class Board: 
    board_id = 0

    # we'll create an m x n board 
    def __init__(self, rows, cols, ):
        board_id += 1
        self.board_id = board_id
        self.rows = rows
        self.cols = cols

# Given an array of characters, the character board, and the board itself, instantiate 
# by creating the positions of the characters


class BoardState:
    def __init__(self, board, characterBoardContainer):
        self.board = board
        self.characterBoardContainer = characterBoardContainer
        self.grid = [[None for col in range(self.board.cols)] for row in range(self.board.rows)]



    def assignCharToGrid(char, position):
        self.grid[position.x][position.y] = char

    def assignCharsToGrid(self):
        for char in self.characterBoardContainer:
            self.assignCharToGrid(char, char.position)

    # def __repr__(self):

