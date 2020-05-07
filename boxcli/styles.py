# Box types dictionary.
box_types = {
    1: {
        "top_right": "+",
        "top_left": "+",
        "bottom_right": "+",
        "bottom_left": "+",
        "horizontal": "-",
        "vertical": "|",
    },
    2: {
        "top_right": "+",
        "top_left": "+",
        "bottom_right": "+",
        "bottom_left": "+",
        "horizontal": " ",
        "vertical": " ",
    },
    3: {
        "top_right": "┓",
        "top_left": "┏",
        "bottom_right": "┛",
        "bottom_left": "┗",
        "horizontal": "━",
        "vertical": "┃",
    },
    4: {
        "top_right": "╮",
        "top_left": "╭",
        "bottom_right": "╯",
        "bottom_left": "╰",
        "horizontal": "─",
        "vertical": "│",
    },
    5: {
        "top_right": "┐",
        "top_left": "┌",
        "bottom_right": "┘",
        "bottom_left": "└",
        "horizontal": "─",
        "vertical": "│",
    },
    6: {
        "top_right": "╗",
        "top_left": "╔",
        "bottom_right": "╝",
        "bottom_left": "╚",
        "horizontal": "═",
        "vertical": "║",
    },
    7: {
        "top_right": "╖",
        "top_left": "╓",
        "bottom_right": "╜",
        "bottom_left": "╙",
        "horizontal": "─",
        "vertical": "║",
    },
    8: {
        "top_right": "╕",
        "top_left": "╒",
        "bottom_right": "╛",
        "bottom_left": "╘",
        "horizontal": "═",
        "vertical": "│",
    }
}

# alignments dictionary
alignments = {
    1: "{sep}{sp}{ln}{os}{sp}{sep}",
    2: "{sep}{px}{ln}{os}{sp}{s}{sep}",
    3: "{sep}{s}{sp}{os}{ln}{px}{sep}"
}
