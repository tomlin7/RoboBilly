from discord.ext import commands

from libs.data import file

from cogs.libs.board import init_board
from cogs.libs.board import show_board
from cogs.libs.board import fen

from cogs.libs.moves import legal_moves
from cogs.libs.moves import legal_move

from cogs.libs.move import push_san
from cogs.libs.move import undo

from cogs.libs.state import checkmate
from cogs.libs.state import stalemate
from cogs.libs.state import insufficient_material
from cogs.libs.state import game_over
from cogs.libs.state import draw

from cogs.libs.repetitions import threefold_repetition
from cogs.libs.repetitions import halfmove_clock
from cogs.libs.repetitions import fifty_moves
from cogs.libs.repetitions import fivefold_repetition
from cogs.libs.repetitions import seventyfive_moves

from cogs.libs.attacks import check
from cogs.libs.attacks import attacked_by
from cogs.libs.attacks import attackers
from cogs.libs.attacks import attacker
from cogs.libs.attacks import attacks


# TODO: aliases for commands. to keep it not too case sensitive.

class Chess(commands.Cog):
    """
    chess game for discord written in python.
    """

    def __init__(self, _bot):
        self.bot = _bot

    @commands.group(name="chess", aliases=["Chess", "c"])
    async def chess(self, _ctx):
        """
        Main function group.
        """
        pass

    @chess.command(name="create", aliases=["Create", "new", "New"])
    async def create_board(self, _ctx, _value=None):
        """
        create a new chess board.
        """
        if _value:
            init_board(_ctx.author.id, _value)
        else:
            init_board(_ctx.author.id)
        await _ctx.send(file=file())

    @chess.command(name="board", aliases=["Board", "chessboard", "showboard"])
    async def board(self, _ctx):
        """
        show user's current chess board.
        """
        show_board(_ctx.author.id)
        await _ctx.send(file=file())

    @chess.command(name="fen", aliases=["FEN", "notation"])
    async def fen(self, _ctx):
        """
        shows FEN notation of user's current chess board.
        """
        await _ctx.send(fen(_ctx.author.id))

    @chess.command(name="moves", aliases=["legalmoves", "possiblemoves"])
    async def moves(self, _ctx):
        """
        shows possible-legal moves for user's current chess board.
        """
        await _ctx.send(legal_moves(_ctx.author.id))

    @chess.group(name="is", aliases=["Is"])
    async def _is(self, _ctx):
        """
        Parent group of checks.
        """
        pass

    @_is.command(name="legal_move", aliases=["legal", "possible"])
    async def legal_move(self, _ctx, _move):
        """
        Checks whether it is a legal move.
        """
        await _ctx.send(legal_move(_ctx.author.id, _move))

    @chess.command(name="move", aliases=["push", "Move", "push_san"])
    async def move(self, _ctx, _move):
        """
        Moves the piece.
        """
        push_san(_ctx.author.id, _move)
        await _ctx.send(file=file())

    @chess.command(name="undo", aliases=["Undo", "pop"])
    async def undo(self, _ctx):
        """
        Undoes the last move.
        """
        undo(_ctx.author.id)
        await _ctx.send(file=file())

    @_is.command(name="checkmate", aliases=["Checkmate", "cm"])
    async def checkmate(self, _ctx):
        """
        Checks whether it is a checkmate.
        """
        await _ctx.send(checkmate(_ctx.author.id))

    @_is.command(name="stalemate", aliases=["Stalemate", "sm"])
    async def stalemate(self, _ctx):
        """
        Checks whether it is a Stalemate
        """
        await _ctx.send(stalemate(_ctx.author.id))

    @_is.command(name="insufficient_material", aliases=["insufficientmaterial", "im"])
    async def insufficient_material(self, _ctx):
        """
        Checks whether neither of the sides have sufficient material to win.
        """
        await _ctx.send(insufficient_material(_ctx.author.id))

    @_is.command(name="game_over", aliases=["gameover", "over"])
    async def game_over(self, _ctx):
        """
        Checks whether the game is over.
        """
        await _ctx.send(game_over(_ctx.author.id))

    # claims group should be created.
    @_is.command(name="draw", aliases=["Draw"])
    async def draw(self, _ctx):
        """
        Checks whether the player can claim a draw.
        """
        await _ctx.send(draw(_ctx.author.id))

    @_is.command(name="threefold_repetition", aliases=["threefold", "threefoldrepetition"])
    async def threefold_repetition(self, _ctx):
        """
        Checks if the player to move can claim a draw by threefold repetition.
        """
        await _ctx.send(threefold_repetition(_ctx.author.id))

    @chess.command(name="halfmove_clock", aliases=["halfmoveclock"])
    async def halfmove_clock(self, _ctx):
        """
        The number of half-moves since the last capture or pawn move.
        """
        await _ctx.send(halfmove_clock(_ctx.author.id))

    @_is.command(name="fifty_moves", aliases=["fiftymoves"])
    async def fifty_moves(self, ctx):
        """
        Checks if the player to move can claim a draw by the fifty-move rule.
        """
        await ctx.send(fifty_moves(ctx.author.id))

    @_is.command(name="fivefold_repetition", aliases=["fivefoldrepetition"])
    async def fivefold_repetition(self, _ctx):
        """
        Checks whether user can claim a draw by fivefold repetition.
        """
        await _ctx.send(fivefold_repetition(_ctx.author.id))

    @_is.command(name="seventyfive_moves", aliases=["seventyfivemoves"])
    async def seventyfive_moves(self, _ctx):
        """
        Checks whether user can claim a draw by seventyfive-moves rule.
        """
        await _ctx.send(seventyfive_moves(_ctx.author.id))

    @_is.command()
    async def check(self, _ctx):
        """
        Checks whether it is a check.
        """
        await _ctx.send(check(_ctx.author.id))

    @_is.command()
    async def attacked_by(self, _ctx, _color, _square):
        """
        Checks whether a piece is attacked by another piece.
        """
        await _ctx.send(attacked_by(_ctx.author.id, _color, _square))

    @chess.command()
    async def attackers(self, _ctx, _color, _square):
        """
        Displays attackers for a piece.
        """
        attackers(_ctx.author.id, _color, _square)
        await _ctx.send(file=file())

    @chess.command()
    async def attacks(self, _ctx, _square):
        """
        Displays attacks on a piece.
        """
        attacks(_ctx.author.id, _square)
        await _ctx.send(file=file())

    @_is.command()
    async def attacker(self, _ctx, _attacker, _color, _square):
        """
        Checks whether a piece is being attacked by another piece.
        """
        await _ctx.send(attacker(_ctx.author.id, _attacker, _color, _square))


def setup(_bot):
    _bot.add_cog(Chess(_bot))
