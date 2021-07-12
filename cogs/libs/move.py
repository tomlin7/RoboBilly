from cogs.libs.boards import boards

from cogs.libs.svg import generate_image


def push_san(_user_id, _move):
    """
    moves a piece.
    """
    _board = boards[_user_id]
    _board.push_san(_move)
    generate_image(_board)


def undo(_user_id):
    """
    undoes a move.
    """
    _board = boards[_user_id]
    _board.pop()
    generate_image(_board)
