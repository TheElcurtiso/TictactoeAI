"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None
BOARD_SIZE = 3


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


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


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        game_won_by = winner(board)
        if game_won_by == X:
            return 1
        elif game_won_by == O:
            return -1
        else:
            return 0


def min_value(board, set_of_maximized_action_values=None):
    minimized_value = math.inf
    if terminal(board):
        return [utility(board), None]
    best_move = None
    best_value_so_far = minimized_value

    value_of_minimized_actions = set()
    for action in actions(board):
        if set_of_maximized_action_values is not None and minimized_value in set_of_maximized_action_values:
            continue

        minimized_value = min(minimized_value, max_value(result(board, action), value_of_minimized_actions)[0])

        value_of_minimized_actions.add(minimized_value)
        if minimized_value < best_value_so_far:
            best_value_so_far = minimized_value
            best_move = action
    return [minimized_value, best_move]


def max_value(board, set_of_minimized_action_values=None):
    maximized_value = -math.inf
    if terminal(board):
        return [utility(board), None]
    best_move = None
    best_value_so_far = maximized_value

    value_of_maximized_actions = set()
    for action in actions(board):
        if set_of_minimized_action_values is not None and maximized_value in set_of_minimized_action_values:
            continue

        maximized_value = max(maximized_value, min_value(result(board, action), value_of_maximized_actions)[0])

        value_of_maximized_actions.add(maximized_value)
        if maximized_value > best_value_so_far:
            best_value_so_far = maximized_value
            best_move = action
    return [maximized_value, best_move]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        return max_value(board)[1]
    elif player(board) == O:
        return min_value(board)[1]
