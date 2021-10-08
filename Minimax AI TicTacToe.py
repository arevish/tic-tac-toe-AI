board = [' ' for x in range(10)]
def printBoard(board):
    print(' ' + board[1] + '| ' + board[2] + '| ' + board[3])
    print('---------')
    print(' ' + board[4] + '| ' + board[5] + '| ' + board[6])
    print('---------')
    print(' ' + board[7] + '| ' + board[8] + '| ' + board[9])

def spaceIsFree(pos):
    return board[pos] == ' '

def insertLetter(letter, pos):
    board[pos] = letter

def isBoardFull(board):
    if board.count(' ')> 1 :
        return False
    else:
        return True

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4]== le and bo[5]== le and bo[6]== le) or (bo[1]== le and bo[2]== le and bo[3]== le) or (bo[1]== le and bo[4]== le and bo[7]== le) or (bo[2]== le and bo[5]== le and bo[8]== le) or (bo[3]== le and bo[6]== le and bo[9]== le) or (bo[1]== le and bo[5]== le and bo[9]== le) or (bo[3]== le and bo[5]== le and bo[7]== le)

def playerMove():
    run = True
    while run:
        move = input("\nPlease select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move <10:
                if spaceIsFree (move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, this space is occupied")
            else:
                print("Please type a number within the range!")
        except:
            print("Please type a number!")

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    bestScore = -1000
    move = 0
    for i in possibleMoves:
        if spaceIsFree(i):
            board[i] = 'O'
            score = minimax(possibleMoves,0,False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                move= i
            
    return move

def minimax(possibleMoves ,state, isMaximizing):
    if isWinner(board, 'O'):
        return 1
    elif isWinner(board, 'X'):
        return -1
    elif isBoardFull(board):
        return 0
    if isMaximizing:
        bestScore = -800
        for i in possibleMoves:
            if spaceIsFree(i):
                board[i] = 'O'
                score = minimax(possibleMoves,state+1,False)
                board[i] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for i in possibleMoves:
            if spaceIsFree(i):
                board[i] = 'X'
                score = minimax(possibleMoves, state+1 , True)
                board[i] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore 

def main():
    print("Welcome to Tic Tac Toe!")
    print('Positions are as follows')
    print(' 1| 2| 3')
    print('---------')
    print(' 4| 5| 6')
    print('---------')
    print(' 7| 8| 9')

    printBoard(board)
    
    if isBoardFull(board):
        print("It's a Tie!")

    while not (isBoardFull(board)):

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0 :
                print("Tie Game!")
            else:
                insertLetter('O', move)
                print("Computer placed an 'O' in position ", move, ":")
                printBoard(board)
        else :
            print("Congrats ! You won the match.")
            break
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else :
            print("Sorry, computer won this match !")
            break
           
main()