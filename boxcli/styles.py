import typing


class RawStyle:
    """Represents the raw style of the box.

    This can be used to specify a custom style.
    You need to pass in a dictionary with the keys,
    ``horizontal``, ``vertical``, ``top_left``, ``top_right``,
    ``bottom_left``, ``bottom_right``, whose values should be
    single character strings or single digit ints. If you pass
    anything else the Box rendering WILL break.


    Arguments
    ---------
    parts : dict
        A dictionary with the format described above.
    """

    def __init__(self, parts: dict) -> None:
        self.horizontal = str(parts.get("horizontal", "-"))
        self.vertical = str(parts.get("vertical", "|"))
        self.top_left = str(parts.get("top_left", "+"))
        self.top_right = str(parts.get("top_right", "+"))
        self.bottom_left = str(parts.get("bottom_left", "+"))
        self.bottom_right = str(parts.get("bottom_right", "+"))


class RGB:
    """Represents a colour in RGB format.

    This can be used to specify a custom box colour with
    preferred RGB colour value.

    Arguments
    ---------
    rgb : typing.Tuple[int, int, int]
        A tuple with the (R, G, B) values.

    Raises
    ------
    ValueError:
        If the values inside the tuple exceed the RGB range.
    """

    def __init__(self, rgb: typing.Tuple[int, int, int]) -> None:
        # Check if the values are valid RGB values.
        for x in rgb:
            if x < 0 or x > 255:
                raise ValueError("Invalid RGB colour.")

        # Create a string out of these values.
        # Mainly to support quick interop with `rich`.
        self.rgb = f"rgb({rgb[0]},{rgb[1]},{rgb[2]})"

    @classmethod
    def from_hex(cls, hex_code: int):
        """Construct an RGB instance from a hex value.

        Arguments
        ---------
        hex_code : int
            The colour hexcode.

        Raises
        ------
        ValueError
            If the hexcode is malformed."""

        if hex_code > 0xFFFFFF or hex_code < 0x000000:
            raise ValueError("Invalid Hex Colour.")

        # Deconstruct the hex code.
        r = (hex_code & 0xFF0000) >> 16
        g = (hex_code & 0x00FF00) >> 8
        b = hex_code & 0x0000FF

        # Return an instance of the class.
        return cls((r, g, b))


# builtin box styles.
default_styles = {
    1: RawStyle(
        {
            "top_right": "+",
            "top_left": "+",
            "bottom_right": "+",
            "bottom_left": "+",
            "horizontal": "-",
            "vertical": "|",
        }
    ),
    2: RawStyle(
        {
            "top_right": "+",
            "top_left": "+",
            "bottom_right": "+",
            "bottom_left": "+",
            "horizontal": " ",
            "vertical": " ",
        }
    ),
    3: RawStyle(
        {
            "top_right": "┓",
            "top_left": "┏",
            "bottom_right": "┛",
            "bottom_left": "┗",
            "horizontal": "━",
            "vertical": "┃",
        }
    ),
    4: RawStyle(
        {
            "top_right": "╮",
            "top_left": "╭",
            "bottom_right": "╯",
            "bottom_left": "╰",
            "horizontal": "─",
            "vertical": "│",
        }
    ),
    5: RawStyle(
        {
            "top_right": "┐",
            "top_left": "┌",
            "bottom_right": "┘",
            "bottom_left": "└",
            "horizontal": "─",
            "vertical": "│",
        }
    ),
    6: RawStyle(
        {
            "top_right": "╗",
            "top_left": "╔",
            "bottom_right": "╝",
            "bottom_left": "╚",
            "horizontal": "═",
            "vertical": "║",
        }
    ),
    7: RawStyle(
        {
            "top_right": "╖",
            "top_left": "╓",
            "bottom_right": "╜",
            "bottom_left": "╙",
            "horizontal": "─",
            "vertical": "║",
        }
    ),
    8: RawStyle(
        {
            "top_right": "╕",
            "top_left": "╒",
            "bottom_right": "╛",
            "bottom_left": "╘",
            "horizontal": "═",
            "vertical": "│",
        }
    ),
}

# alignments dictionary
alignments = {
    1: "{sep}{sp}{ln}{os}{sp}{sep}",
    2: "{sep}{px}{ln}{os}{sp}{s}{sep}",
    3: "{sep}{s}{sp}{os}{ln}{px}{sep}",
}

# colour list
colours_list = {
    1: "black",
    2: "red",
    3: "green",
    4: "blue",
    5: "cyan",
    6: "magenta",
    7: "yellow",
    8: "white",
}
