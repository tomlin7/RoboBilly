import chess
import chess.svg

from cogs.libs.svg import generate_image

from cogs.libs.boards import boards


def convert(_value):
    """
    converts values white, black to booleans.
    """
    values = [1, 0]
    if _value not in values:
        if _value.lower() == "white":
            return True
        elif _value.lower() == "black":
            return False
    else:
        return _value


def check(_user_id):
    """
    checks whether it is a check.
    """
    _board = boards[_user_id]
    return _board.is_check()


def attacked_by(_user_id, _color, _square):
    """
    checks whether a piece is attacked by a side.
    """
    _board = boards[_user_id]
    return _board.is_attacked_by(convert(_color), chess.parse_square(_square))


def attackers(_user_id, _color, _square):
    """
    displays attackers for a piece.
    """
    _board = boards[_user_id]
    squares = _board.attackers(convert(_color), chess.parse_square(_square))
    generate_image(_board, _squares=squares)


def attacker(_user_id, _attacker, _color, _square):
    """
    checks whether a piece is being attacked by another piece.
    """
    _board = boards[_user_id]
    _attackers = _board.attackers(convert(_color), chess.parse_square(_square))
    return chess.parse_square(_attacker) in _attackers


def attacks(_user_id, _square):
    """
    displays attacks on a piece.
    """
    _board = boards[_user_id]
    _attacks = _board.attacks(chess.parse_square(_square))
    generate_image(_board, _squares=_attacks)
