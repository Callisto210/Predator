import random

def getPositions(board):
    listOfX = []
    listOfO = []
    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE):
            if board[i, j] is 'X':
                listOfX.append((i, j))
            elif board[i, j] is 'O':
                listOfO.append((i, j))
    return listOfX, listOfO

def getUsableFields(board, myMark):
    listOfFreeFields = []
    for i in {0, BOARD_SIZE-1}:
        for j in range(0, BOARD_SIZE):
            if board[i, j] in {'', myMark}:
                listOfFreeFields.append((i, j))
            if board[j, i] in {'', myMark}:
                listOfFreeFields.append((j, i))
    return listOfFreeFields

def sumPoints():
    colsX = [0 for _ in range(BOARD_SIZE)]
    rowsX = [0 for _ in range(BOARD_SIZE)]
    colsO = [0 for _ in range(BOARD_SIZE)]
    rowsO = [0 for _ in range(BOARD_SIZE)]

    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE):
            if board[i, j] is 'X':
                rowsX[i] += 1
                colsX[j] += 1
            elif board[i, j] is 'O':
                rowsO[i] += 1
                colsO[j] += 1

    return rowsX, colsX, rowsO, colsO

def isMarkWinning(pointsX, pointsO, mark):
    maxX = max(pointsX)
    maxO = max(pointsO)
    if maxX > maxO:
        if mark == 'X':
            return True
        else:
            return False
    elif maxX < maxO:
        if mark == 'O':
            return True
        else:
            return False
    else:
        return False

class Player:

    def __init__(self):
        pass

    def setMaxIterationNumber(self, maxNumber):
        pass

    def setTypeOfAssignedMark(self, mark):
        self.myMark = mark
        print("Assigned mark: " + self.myMark)

    def setStateOfGameField(self, gameField):
        self.board = gameField

    def setInformationAboutDisqualification(self, info):
        if info:
            print("Jak to się mogło stać!!! Panie sędzio ja niechcący ;D")

    def setInformationAboutGameEnd(self, info):
        if info:
            print("Ktoś powiedział coś o końcu gry?")

    def setInformationAboutWinning(self, info):
        if info == True:
            print("Wygrałem? Naprawdę wygrałem HURA!!!!")
        elif info == False:
            print("Serio?")
        else:
            print("Meh...")

    def makeMove(self):
        pass    
