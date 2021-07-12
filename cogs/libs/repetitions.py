from cogs.libs.boards import boards


def threefold_repetition(_user_id):
    """
    Checks if the player to move can claim a draw by threefold repetition.

    Draw by threefold repetition can be claimed if the position on the board occured for the third time
    or if such a repetition is reached with one of the possible legal moves.
    """
    _board = boards[_user_id]
    return _board.can_claim_threefold_repetition()


def halfmove_clock(_user_id):
    """
    The number of half-moves since the last capture or pawn move.
    """
    _board = boards[_user_id]
    return _board.halfmove_clock


def fifty_moves(_user_id):
    """
    Checks if the player to move can claim a draw by the fifty-move rule.

    Draw by the fifty-move rule can be claimed once the clock of halfmoves since the last capture
    or pawn move becomes equal or greater to 100, or if there is a legal move that achieves this.
    Other means of ending the game take precedence.
    """
    _board = boards[_user_id]
    return _board.can_claim_fifty_moves()


def fivefold_repetition(_user_id):
    """
    Since the 1st of July 2014 a game is automatically drawn (without a claim by one of the players)
    if a position occurs for the fifth time. Originally this had to occur on consecutive alternating moves,
    but this has since been revised.
    """
    _board = boards[_user_id]
    return _board.is_fivefold_repetition()


def seventyfive_moves(_user_id):
    """
    Since the 1st of July 2014, a game is automatically drawn (without a clain by one of the players)
    if the half-move clock since a capture or pawn move is equal to or greater than 150.
    Other means to end a game take precedence.
    """
    _board = boards[_user_id]
    return _board.is_seventyfive_moves()
