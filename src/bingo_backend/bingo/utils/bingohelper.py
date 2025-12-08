bingo_conditions = {
    "r1": {
        "name": "Row 1",
        "spaces": [0, 1, 2, 3, 4]
},
    "r2": {
        "name": "Row 2",
        "spaces": (5, 6, 7, 8, 9),
    },
    "r3": {
        "name": "Row 3",
        "spaces": (10, 11, 12, 13, 14),
    },
    "r4": {
        "name": "Row 4",
        "spaces": (15, 16, 17, 18, 19),
    },
    "r5": {
        "name": "Row 5",
        "spaces": (20, 21, 22, 23, 24),
    },
    "c1": {
        "name": "Column 1",
        "spaces": (0, 5, 10, 15, 20),
    },
    "c2": {
        "name": "Column 2",
        "spaces": (1, 6, 11, 16, 21),
    },
    "c3": {
        "name": "Column 3",
        "spaces": (2, 7, 12, 17, 22),
    },
    "c4": {
        "name": "Column 4",
        "spaces": (3, 8, 13, 18, 23),
    },
    "c5": {
        "name": "Column 5",
        "spaces": (4, 9, 14, 19, 24),
    },
    "dr": {
        "name": "Diagonal Right",
        "spaces": (0, 6, 12, 18, 24),
    },
    "dl": {
        "name": "Diagonal Left",
        "spaces": (4, 8, 12, 16, 20)
    },
    "fc": {
        "name": "Four Corners",
        "spaces": (0, 4, 20, 24)
    }
}

def check_has_bingo(spaces, space):
    remaining_spaces = 5
    for condition in bingo_conditions.values():
        if space in condition["spaces"]:
            if set(spaces).issuperset(condition["spaces"]):
                return True, 0, condition["name"]
            else:
                space_count = len(set(spaces).intersection(condition["spaces"]))
                if 5 - space_count < remaining_spaces:
                    remaining_spaces = 5 - space_count

    return False, remaining_spaces, None