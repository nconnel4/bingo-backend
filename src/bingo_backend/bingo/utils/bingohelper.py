bingo_conditions = (
    (0, 1, 2, 3, 4),
    (5, 6, 7, 8, 9),
    (10, 11, 12, 13, 14),
    (15, 16, 17, 18, 19),
    (20, 21, 22, 23, 24),
    (0, 5, 10, 15, 20),
    (1, 6, 11, 16, 21),
    (2, 7, 12, 17, 22),
    (3, 8, 13, 18, 23),
    (4, 9, 14, 19, 24),
    (0, 6, 12, 18, 24),
    (4, 8, 13, 16, 20)
)

def check_has_bingo(spaces, space):
    remaining_spaces = 5
    for condition in bingo_conditions:
        if space in condition:
            if set(spaces).issuperset(condition):
                return True, 0
            else:
                space_count = len(set(spaces).intersection(condition))
                if 5 - space_count < remaining_spaces:
                    remaining_spaces = 5 - space_count

    return False, remaining_spaces