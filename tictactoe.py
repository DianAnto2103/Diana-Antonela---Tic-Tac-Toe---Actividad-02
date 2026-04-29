"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    conteo_x = 0
    conteo_o = 0

    for i in range(3):
        for j in range(3): 
            if board[i][j] == X:
                conteo_x+=1
            elif board[i][j] == O:
                conteo_o+=1

    if(conteo_x == conteo_o):
        return X
    else:
        return O
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acciones_posibles = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acciones_posibles.add((i,j))
            else:
                pass
    return acciones_posibles
    

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("La acción no se encuentra disponible.")
    
    copia_profunda = copy.deepcopy(board)

    fila,columna = action 

    copia_profunda[fila][columna] = player(copia_profunda)

    return copia_profunda

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
