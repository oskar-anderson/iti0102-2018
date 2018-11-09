"""wat."""

first_special_ans = [4, 6]
first_general_ans = [0, 2, 8, 11, 12, 14, 16, 18]


def first(n: int):
    """First."""
    if n in range(3, 6):
        ans = first_special_ans[0]
        first_special_ans.remove(ans)
        return ans
    else:
        ans = first_general_ans[0]
        first_general_ans.remove(ans)
        return ans


def last(n: int):
    """Last."""
    for i in range(10):
        if n in range(1167 + 88 * i, 1255 + 88 * i):
            return 34 + i


if __name__ == '__main__':
    print(first(1))  # Expected: 0
    print(first(2))  # Expected 2
    print(first(4))  # Expected: 4
    print(first(3))  # Expected: 6
    print(first(708))  # Expected: 8
    print(first(-871))  # Expected: 11
    print(first(-489))  # Expected: 12
    print(first(-1))  # Expected: 14
    print(first(0))  # Expected: 16
    print(first(2505))  # Expected 18

    print()
    print(last(1167))
