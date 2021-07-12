from chess import svg

from cairosvg import svg2png


def get_image(_svg_code):
    """
    Convert the SVG string to PNG.
    """
    svg2png(bytestring=_svg_code, write_to='output.png')


def generate_image(_board, _squares=None):
    """
    Generate SVG string of the board.
    """
    if _squares:
        get_image(svg.board(_board, squares=_squares, size=350))
    else:
        get_image(svg.board(_board, size=350))
