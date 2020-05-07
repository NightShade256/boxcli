__all__ = ["TitlePositionError", "TitleLengthError", "DifferentLengthError"]


class TitlePositionError(Exception):
    """Raised when the title position is not INSIDE and the title
    contains a newline character."""
    pass


class TitleLengthError(Exception):
    """Raised when the title length is larger than the length of the top
    and bottom bars."""
    pass


class DifferentLengthError(Exception):
    """Raised when the length of the top bar doesn't match the length of
    the bottom bar."""
    pass
