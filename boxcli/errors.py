__all__ = ["TitlePositionError", "TitleLengthError"]


class TitlePositionError(Exception):
    """Raised when the title position is inside and title has multiple lines."""

    pass


class TitleLengthError(Exception):
    """Raised when title length is larger than the top and bottom bars."""

    pass
