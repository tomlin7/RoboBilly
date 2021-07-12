from cogs.libs.boards import boards


def checkmate(_user_id):
    """
    Checks if the current position is a checkmate.
    """
    _board = boards[_user_id]
    return _board.is_checkmate()


def stalemate(_user_id):
    """
    Checks if the current position is a stalemate.
    """
    _board = boards[_user_id]
    return _board.is_stalemate()


def insufficient_material(_user_id):
    """
    Checks if neither side has sufficient winning material.
    """
    _board = boards[_user_id]
    return _board.is_insufficient_material()


def game_over(_user_id):
    """
    Checks whether the game is over due to...
    - checkmate
    - stalemate
    - insufficient_material

    - seventyfive-move rule
    - fivefold repetition
    """
    _board = boards[_user_id]
    return _board.is_game_over()


def draw(_user_id):
    """
    Checks if the player to move can claim a draw by the fifty-move rule
    or by threefold repetition.
    """
    _board = boards[_user_id]
    return _board.can_claim_draw()
