boardSize = input("Enter the board size:")
print(f"Prepare a {boardSize}x{boardSize} board ...")
player1 = input("Enter the first player name:")
print(f"Player 1 is {player1} !!!")
player2 = input("Enter the second player name:")
print(f"Player 2 is {player2} !!!")
boardSize = int(boardSize)
totalMoves = 0
currPlayer = 0






def printBoard(board):
    boardCopy = board.copy()
    all_ = []
    for i in range(len(boardCopy)):
        row = " ".join(boardCopy[i])
        all_ += [row]
    return "\n".join(all_)


currentBoard = [["_" for i in range(boardSize)] for _ in range(boardSize)]
boardString = printBoard(currentBoard)
print(boardString)
# print(f"currentBoard: {currentBoard}")

def containsStringOnly(inputStr):
    for char in inputStr:
        if not char.isdigit():
            return False
    return True

def checkInput(inputStr):
    if "," not in inputStr:
        return False, "Please add a second input for column!"
    row, col = [i for i in inputStr.split(",")]
    if len(row) == 0 or len(col) == 0:
        return False, "Please add valid inputs of string length of more than 0!"
    if not containsStringOnly(row) or not containsStringOnly(col):
        return False, "Please enter a digit for inputs!"

    return True, "Success!"


def checkWinner(board):
    

    first = board[0][0]
    while counter < len(board):
        if board[counter][counter] != first:
            break
        counter += 1

    if counter == len(board):
        return True, first

    for i in range(len(board)):
        counter = 0
        first = board[i][0]
        for j in range(1,len(board[i])):
            if board[j][i] != first:
                break
        if counter == len(board):
            break

    

while totalMoves < boardSize**2:

    if currPlayer == 0:
        player1_input = input(f"{player1}, please enter a coordinate to put “X”: ")

        valid, errMsg = checkInput(player1_input)
        while not valid:
            # print(f"Error: {errMsg}")
            # John, the coordinate can not be identified, please enter a new coordinate: 
            player1_input = input(f"{player1}, please enter a coordinate to put “X”: ")
            # break
            row, col = [int(i) for i in player1_input.split(",")]
            print(f"row: {row}, col: {col}")
            currPlayer = 0
            valid, errMsg = checkInput(player1_input)

        row, col = [int(i) for i in player1_input.split(",")]
        
        print(f"row: {row}, col: {col}")
        currPlayer = 1


        while currentBoard[row-1][col-1] != "_":
            # print(f"Error: {errMsg}")
            # John, the coordinate can not be identified, please enter a new coordinate: 
            if currentBoard[row-1][col-1] == "X":
                currentPlayer = player1
            else:
                currentPlayer = player2
            player1_input = input(f"{currentPlayer}, John has already put “{currentBoard[row-1][col-1]}” in this position, please enter a new coordinate:  ")
            # break
            row, col = [int(i) for i in player1_input.split(",")]
            print(f"row: {row}, col: {col}")
            currPlayer = 0
            valid, errMsg = checkInput(player1_input)

        currentBoard[row-1][col-1] = "X"
        # print(currentBoard)

    elif currPlayer == 1:
        player2_input = input(f"{player2}, please enter a coordinate to put “O”: ")
        row, col = [int(i) for i in player2_input.split(",")]
        print(f"row: {row}, col: {col}")
        currPlayer = 0
        valid, errMsg = checkInput(player1_input)
        while not valid:
            # print(f"Error: {errMsg}")
            # John, the coordinate can not be identified, please enter a new coordinate: 
            player2_input = input(f"{player1}, please enter a coordinate to put “X”: ")
            # break
            row, col = [int(i) for i in player2_input.split(",")]
            print(f"row: {row}, col: {col}")
            currPlayer = 0
            valid, errMsg = checkInput(player2_input)



        currentBoard[row-1][col-1] = "O"
        # print(currentBoard)

    totalMoves += 1
    boardString = printBoard(currentBoard)
    print(f"boardString: \n{boardString}")

    

    
# print("Username is: " + username)