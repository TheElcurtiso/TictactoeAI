from tictactoe import initial_state
import copy

X = "X"
O = "O"
EMPTY = None
BOARD_SIZE = 3


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_O = 0
    number_of_X = 0
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if board[row][column] == O:
                number_of_O += 1
            elif board[row][column] == X:
                number_of_X += 1
    if number_of_O < number_of_X:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    valid_actions = set()
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if board[row][column] == EMPTY:
                valid_actions.add((row, column))
    return valid_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copied_board = copy.deepcopy(board)
    if action not in actions(copied_board):
        raise IndexError
    copied_board[action[0]][action[1]] = player(copied_board)
    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    number_of_X = 0
    number_of_O = 0
    # horizontal victory
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if board[row][column] == X:
                number_of_X += 1
                if number_of_X == 3:
                    return X
            elif board[row][column] == O:
                number_of_O += 1
                if number_of_O == 3:
                    return O
        number_of_X = 0
        number_of_O = 0

    # vertical victory
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if board[column][row] == X:
                number_of_X += 1
                if number_of_X == 3:
                    return X
            elif board[column][row] == O:
                number_of_O += 1
                if number_of_O == 3:
                    return O
        number_of_X = 0
        number_of_O = 0

    # left diagonal victory
    for row in range(BOARD_SIZE):
        if board[row][row] == X:
            number_of_X += 1
        elif board[row][row] == O:
            number_of_O += 1
    if number_of_X == 3:
        return X
    elif number_of_O == 3:
        return O

    number_of_X = 0
    number_of_O = 0
    # right diagonal victory
    column = BOARD_SIZE - 1
    for row in range(BOARD_SIZE):
        if board[row][column] == X:
            number_of_X += 1
        elif board[row][column] == O:
            number_of_O += 1
        column -= 1
    if number_of_X == 3:
        return X
    elif number_of_O == 3:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or every_space_has_been_filled(board):
        return True
    return False


def every_space_has_been_filled(board):
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if board[row][column] == EMPTY:
                return False
    return True
