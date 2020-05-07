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

    def __init__(self, parts: dict):
        self.horizontal = str(parts.get("horizontal", "-"))
        self.vertical = str(parts.get("vertical", "|"))
        self.top_left = str(parts.get("top_left", "+"))
        self.top_right = str(parts.get("top_right", "+"))
        self.bottom_left = str(parts.get("bottom_left", "+"))
        self.bottom_right = str(parts.get("bottom_right", "+"))


# builtin box styles.
default_styles = {
    1: RawStyle({
        "top_right": "+",
        "top_left": "+",
        "bottom_right": "+",
        "bottom_left": "+",
        "horizontal": "-",
        "vertical": "|",
    }),
    2: RawStyle({
        "top_right": "+",
        "top_left": "+",
        "bottom_right": "+",
        "bottom_left": "+",
        "horizontal": " ",
        "vertical": " ",
    }),
    3: RawStyle({
        "top_right": "┓",
        "top_left": "┏",
        "bottom_right": "┛",
        "bottom_left": "┗",
        "horizontal": "━",
        "vertical": "┃",
    }),
    4: RawStyle({
        "top_right": "╮",
        "top_left": "╭",
        "bottom_right": "╯",
        "bottom_left": "╰",
        "horizontal": "─",
        "vertical": "│",
    }),
    5: RawStyle({
        "top_right": "┐",
        "top_left": "┌",
        "bottom_right": "┘",
        "bottom_left": "└",
        "horizontal": "─",
        "vertical": "│",
    }),
    6: RawStyle({
        "top_right": "╗",
        "top_left": "╔",
        "bottom_right": "╝",
        "bottom_left": "╚",
        "horizontal": "═",
        "vertical": "║",
    }),
    7: RawStyle({
        "top_right": "╖",
        "top_left": "╓",
        "bottom_right": "╜",
        "bottom_left": "╙",
        "horizontal": "─",
        "vertical": "║",
    }),
    8: RawStyle({
        "top_right": "╕",
        "top_left": "╒",
        "bottom_right": "╛",
        "bottom_left": "╘",
        "horizontal": "═",
        "vertical": "│",
    })
}

# alignments dictionary
alignments = {
    1: "{sep}{sp}{ln}{os}{sp}{sep}",
    2: "{sep}{px}{ln}{os}{sp}{s}{sep}",
    3: "{sep}{s}{sp}{os}{ln}{px}{sep}"
}
