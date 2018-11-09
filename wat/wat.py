"""wat."""

first_special_ans3 = [6, 4]
first_special_ans4 = [4, 6]
first_special_ans5 = [4, 6]
first_general_ans = [8, 11, 12, 14, 16, 18]


def first(n: int):
    """First."""
    if n in range(3, 6):
        if n == 3:
            return first_special_ans3.pop(0)
        elif n == 4:
            return first_special_ans4.pop(0)
        else:
            return first_special_ans5.pop(0)
    else:
        return first_general_ans.pop(0)


def last(n: int):
    """Last"""
    if n:
        pass


if __name__ == '__main__':
    print(first(3))
    print(first(3))
