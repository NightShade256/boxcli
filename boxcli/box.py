import enum
from typing import List, Union

from colorama import Fore
from wcwidth import wcswidth

from .errors import DifferentLengthError, TitleLengthError, TitlePositionError
from .styles import RawStyle, alignments, colours_list, default_styles

__all__ = ["BoxStyles", "ContentAlignment", "TitlePosition", "BoxFactory", "ColourEnum"]


def _longest_line(lines: List[str]) -> int:
    """Returns the length of the longest line.

    Arguments
    ---------
    lines : list[str]
        A list of lines

    Returns
    -------
    int
        The length of the longest line."""

    longest = 0
    for line in lines:
        if wcswidth(line) > longest:
            longest = wcswidth(line)
    return longest


class BoxStyles(enum.Enum):
    """BoxStyle enumeration, to be used to specify the box style.

    To see the box styles for yourself please go to the project README.

    Attributes
    ----------
    CLASSIC : BoxStyles
        The classic box style, with plus signs at the corners
        and dashes as the separators.
    INVISIBLE : BoxStyles
        The invisible box style, with plus signs at the corners
        but no box outline separators.
    BOLD : BoxStyles
        The bold box style.
    ROUND : BoxStyles
        The round box style, with rounded edges.
    SINGLE : BoxStyles
        The single box style.
    DOUBLE : BoxStyles
        The double box style, similar to the single box style
        but has two lines in the separators and corners instead
        of single line.
    SINGLE_DOUBLE : BoxStyles
        The single double box style.
    DOUBLE_SINGLE : BoxStyles
        The double single box style.
    """

    CLASSIC = 1
    INVISIBLE = 2
    BOLD = 3
    ROUND = 4
    SINGLE = 5
    DOUBLE = 6
    SINGLE_DOUBLE = 7
    DOUBLE_SINGLE = 8


class ContentAlignment(enum.Enum):
    """Content alignment enumeration.

    To be used to specify the alignment of the content and title in
    the box.

    Attributes
    ----------
    CENTRE : ContentAlignment
        Centred alignment.
    LEFT : ContentAligment
        Left-sided alignment.
    RIGHT : ContentAlignment
        Right-sided alignment.
    """

    CENTRE = 1
    LEFT = 2
    RIGHT = 3


class TitlePosition(enum.Enum):
    """Title Position enumeration.

    To be used to specify the position of the title relative to
    the box.

    Attributes
    ----------
    INSIDE : TitlePosition
        The title position inside the box with the content.
    TOP : TitlePosition
        The title position on top of the box.
    BOTTOM : TitlePosition
        The title position underneath the box.
    """

    INSIDE = 1
    TOP = 2
    BOTTOM = 3


class ColourEnum(enum.Enum):
    """The colour enumeration, can be used to specify colour of box border.

    Attributes
    -----------
    BLACK : ColourEnum
        Black Colour.
    RED : ColourEnum
        Red Colour.
    GREEN : ColourEnum
        Green Colour.
    BLUE : ColourEnum
        Blue Colour.
    CYAN : ColourEnum
        Cyan Colour.
    MAGENTA : ColourEnum
        Magenta Colour.
    YELLOW : ColourEnum
        Yellow Colour.
    WHITE : ColourEnum
        White Colour.
    """

    BLACK = 1
    RED = 2
    GREEN = 3
    BLUE = 4
    CYAN = 5
    MAGENTA = 6
    YELLOW = 7
    WHITE = 8


class BoxFactory:
    """Represents a Box factory.

    This class can be used to create terminal boxes with ease.

    Arguments
    ---------
    Px : int
        Horizontal padding.
    Py : int
        Vertical padding.
    style : Union[BoxStyles, RawStyle]
        The style used to construct boxes.
        You can pass in a BoxStyles enum for builtin styles.
        or use boxcli.RawStyle to specify a custom one.

    Keyword Arguments
    -----------------
    alignment : ContentAlignment
        The alignment used to construct boxes.
        Defaults to ContentAlignment.CENTRE
    title_pos : TitlePosition
        The position of the title with respect to the box.
        Defaults to TitlePosition.INSIDE
    colour : ColourEnum
        The colour to be used to construct the box border.
        Defaults to None.
    """

    def __init__(self, Px: int, Py: int, style: Union[BoxStyles, RawStyle], **kwargs):
        """The constructor nothing to explain here."""
        self.Px = Px
        self.Py = Py
        if isinstance(style, BoxStyles):
            self.style = default_styles.get(style.value)
        else:
            self.style = style
        self.alignment = kwargs.get("alignment", ContentAlignment.CENTRE)
        self.title_position = kwargs.get("title_pos", TitlePosition.INSIDE)
        self.colour = kwargs.get("colour", None)
        if self.colour is not None:
            self.colour = colours_list.get(self.colour.value)

    def _add_vert_padding(self, length: int) -> list:
        """Returns a list of lines with vertical separators.

        The amount of lines returned corresponds to the
        vertical padding value.

        Arguments
        ---------
        length : int
            Length of the longest line.

        Returns
        -------
        list[str]
            Lines equvivalent in number to the vertical padding,
            with end separators.
        """
        # Here note that the two we subtract corresponds to the
        # end separators.
        padding = " " * (length - 2)
        lines = []
        if self.colour is not None:
            sep = f"{self.colour}{self.style.vertical}{Fore.RESET}"
        else:
            sep = self.style.vertical
        for _ in range(self.Py):
            lines.append(sep + padding + sep)
        return lines

    def _repeat_with_string(self, c: str, s: str, n: int) -> str:
        """Returns the title of the box with separators.

        This is only called when the title position is
        TitlePosition.TOP or TitlePosition.BOTTOM

        Arguments
        ---------
        c : str
            The separator
        s : str
            The title of the box
        n : int
            Computed width of the box.

        Returns
        -------
        str
            The title of the box with appended separators."""

        count = n - wcswidth(s) - 2
        if self.colour is not None:
            bar = f"{self.colour}{c * count}{Fore.RESET}"
        else:
            bar = c * count
        return f" {s} {bar}"

    def get_box(self, title: str, content: str) -> str:
        """Returns a rendered box in the form of a string.

        Arguments
        ---------
        title : str
            The title of the box.
        content : str
            The content of the box.

        Returns
        -------
        str
            The rendered box with the title and content
            provided by the user.

        Raises
        ------
        TitlePositionError
            If the position of the title is not TitlePosition.INSIDE
            and yet it contains a newline.
        TitleLengthError
            If the length of the title is larger than the
            length of the largest line in the content.
        DifferentLengthError
            If the length of the top bar is not equal to the
            length of the bottom bar.
        """
        # side_margin here refers to the horizontal padding.
        side_margin = " " * self.Px

        # compute the longest line
        longest_line = _longest_line(content.splitlines())
        if self.title_position == TitlePosition.INSIDE:
            if wcswidth(title) > longest_line:
                longest_line = wcswidth(title)

        lines = []

        # n here is essentially the width of the rendered box
        # including the separators at the end.
        n = longest_line + (self.Px * 2) + 2

        # Check if the title is violating one of two things
        # 1) Title is outside the box and contains a new line.
        # 2) Title is longer than the length of the top and bottom bars.
        if self.title_position != TitlePosition.INSIDE and "\n" in title:
            raise TitlePositionError()

        if self.title_position != TitlePosition.INSIDE and wcswidth(title) > n - 2:
            raise TitleLengthError()

        if self.title_position == TitlePosition.INSIDE:
            lines.extend(title.splitlines())
            lines.append("")

        # Create temporary top and bottom bars.
        bar = self.style.horizontal * (n - 2)
        top_bar = self.style.top_left + bar + self.style.top_right
        bottom_bar = self.style.bottom_left + bar + self.style.bottom_right

        if self.colour is not None:
            top_bar = f"{self.colour}{top_bar}{Fore.RESET}"
            bottom_bar = f"{self.colour}{bottom_bar}{Fore.RESET}"

        # Update the bars if the position of the title is other than
        # that of inside the box.
        if self.title_position != TitlePosition.INSIDE:
            title_bar = self._repeat_with_string(self.style.horizontal, title, n - 2)
            if self.title_position == TitlePosition.TOP:
                if self.colour is not None:
                    top_bar = (
                        f"{self.colour}{self.style.top_left}{Fore.RESET}"
                        + title_bar
                        + f"{self.colour}{self.style.top_right}{Fore.RESET}"
                    )
                else:
                    top_bar = self.style.top_left + title_bar + self.style.top_right
            elif self.title_position == TitlePosition.BOTTOM:
                if self.colour is not None:
                    bottom_bar = (
                        f"{self.colour}{self.style.bottom_left}{Fore.RESET}"
                        + title_bar
                        + f"{self.colour}{self.style.bottom_right}{Fore.RESET}"
                    )
                else:
                    bottom_bar = (
                        self.style.bottom_left + title_bar + self.style.bottom_right
                    )

        # Check if the length of the top and bottom bars match
        # if the title is inside the box.
        temp_cond = wcswidth(top_bar) != wcswidth(bottom_bar)
        if self.title_position == TitlePosition.INSIDE and temp_cond:
            raise DifferentLengthError()

        # texts is a list that will eventually
        # contain the rendered lines other than the top and bottom bars.
        # Right now though it just contains the vertical padding lines.
        texts = self._add_vert_padding(n)

        # This just splits the content in its constituent lines.
        # and appends them to the lines list.
        lines.extend(content.splitlines())

        # This loop renders the title and the content.
        for item in lines:
            length = wcswidth(item)

            # Odd space is the space that needs to be added in a line if
            # difference in the length of the current line and the longest
            # line is odd. This fixes oddities in rendering.
            space, odd_space = "", ""

            # Calculate spacing and odd_space
            if length < longest_line:
                diff = longest_line - length
                to_add = diff / 2
                space = " " * int(to_add)
                if diff % 2 != 0:
                    odd_space = " "

            # 'Render' the line using the format function.
            if self.colour is not None:
                sep = f"{self.colour}{self.style.vertical}{Fore.RESET}"
            else:
                sep = self.style.vertical
            spacing = str(space) + str(side_margin)
            fmt_string = alignments[self.alignment.value]
            box_string = fmt_string.format(
                sep=sep, sp=spacing, ln=item, os=odd_space, s=space, px=side_margin,
            )

            # Add the line to our list of lines.
            texts.append(box_string)

        # The padding here is added to maintain symmetry of the
        # top and bottom halves of the box.
        vertpadding = self._add_vert_padding(n)
        texts.extend(vertpadding)

        # joint_lines is just the rendered lines joint by a new line
        # I just added this variable so I could comply with PEP8 :P
        joint_lines = "\n".join(texts)

        # Finally after all that return the 'rendered' box.
        return f"{top_bar}\n{joint_lines}\n{bottom_bar}\n"

    def update(self, **kwargs) -> None:
        """Update the settings of the box factory.

        Keyword Arguments
        -----------------
        Px : int
            The horizontal padding.
        Py : int
            The vertical padding.
        style : Union[BoxStyles, RawStyle]
            The style used to construct boxes
        alignment : ContentAlignment
            The alignment of the content and title.
        title_pos : TitlePosition
            The position of the title relative to the box.
        colour : ColourEnum
            The colour of the box border.
        """
        self.Px = kwargs.get("Px", self.Px)
        self.Py = kwargs.get("Py", self.Py)
        style_temp = kwargs.get("style", self.style)
        if isinstance(style_temp, BoxStyles):
            self.style = default_styles.get(style_temp)
        else:
            self.style = style_temp
        self.alignment = kwargs.get("alignment", self.alignment)
        self.title_position = kwargs.get("title_pos", self.title_position)
        self.colour = kwargs.get("colour", self.colour)
        if self.colour is not None:
            self.colour = colours_list.get(self.colour.value)
