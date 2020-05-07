__all__ = ["TitlePositionError", "TitleLengthError", "DifferentLengthError"]


class TitlePositionError(Exception):
    """Raised when the title position is inside and title has multiple lines."""

    pass


class TitleLengthError(Exception):
    """Raised when title length is larger than the top and bottom bars."""

    pass


class DifferentLengthError(Exception):
    """Raised when the length of top bar is not equal to that of bottom bar."""

    pass
